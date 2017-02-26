import collections

def stan(*conf):
	conf = unmod(*conf)
	conf = merge(*conf)
	conf = unval(conf)
	conf = default(conf)
	conf = analyze(conf)

	return conf

def unmod(*conf):
	return tuple({ k:v for k, v in vars(conf).items() if "__" not in k } for conf in conf)

def merge(*conf):
	merged = {}

	for conf in conf:
		merged.update(conf)

	return merged

def unval(conf):
	val = conf["val"]

	# setup val replace
	for k, v in conf["setup"].items():
		if k in val:
			conf["setup"][k] = _rec_unval(v, val[k])

	# rank val replace
	if "rank" in conf:
		for item in conf["rank"]:
			if item["key"] in val:
				item["val"] = _rec_unval(item["val"], val[item["key"]])

	return conf

def _rec_unval(v, val):
	if isinstance(v, str):
		return val[v]

	if isinstance(v, tuple):
		return tuple(_rec_unval(v, val) for v in v)

	if isinstance(v, list):
		return [ _rec_unval(v, val) for v in v ]

	if isinstance(v, dict):
		return { k : _rec_unval(v, val) for k, v in v.items() }

	return v

def default(conf):
	default = conf["default"]

	# default setup
	for k, v in default.items():
		conf["setup"].setdefault(k, v)

	# default rank list
	if "rank" in conf:
		for rule in conf["rank"]:
			if (not isinstance(rule["val"], dict)
					and not isinstance(rule["val"], list)):
				rule["val"] = [ rule["val"] ]

	return conf

def analyze(conf):
	al = {
		"exact" : set(),
		"range" : set(),
		"keys" : {}
	}

	if "rank" in conf:
		for i, rule in enumerate(conf["rank"]):
			key = rule["key"]
			val = rule["val"]

			# keys
			al["keys"].setdefault(key, set())
			al["keys"][key].add(i)

			# vals
			if isinstance(val, list):
				al["exact"].add(i)

			if isinstance(val, dict):
				al["range"].add(i)

	conf["tmp"]["analysis"] = al
	return conf

def update(d, u):
	for k, v in u.items():
		if isinstance(v, collections.Mapping):
			r = update(d.get(k, {}), v)
			d[k] = r
		else:
			d[k] = u[k]

	return d

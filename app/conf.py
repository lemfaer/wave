def stan(*conf):
	conf = unmod(*conf)
	conf = lower(*conf)
	conf = merge(*conf)
	conf = unval(conf)
	conf = default(conf)

	return conf

def unmod(*conf):
	return tuple({ k:v for k, v in vars(conf).items() if "__" not in k } for conf in conf)

def lower(*conf):
	return tuple(_rec_lower(conf) for conf in conf)

def _rec_lower(v):
	if isinstance(v, str):
		return v.lower()

	if isinstance(v, list):
		return [ _rec_lower(v) for v in v ]

	if isinstance(v, tuple):
		return tuple(_rec_lower(v) for v in v)

	if isinstance(v, dict):
		return { _rec_lower(k):_rec_lower(v) for k, v in v.items() }

	return v

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

	# mark val replace
	if "mark" in conf:
		for item in conf["mark"]:
			if item["name"] in val:
				item["value"] = _rec_unval(item["value"], val[item["name"]])

	return conf

def _rec_unval(v, val):
	if isinstance(v, str):
		return val[v]

	if isinstance(v, list):
		return [ _rec_unval(v, val) for v in v ]

	if isinstance(v, tuple):
		return tuple(_rec_unval(v, val) for v in v)

	return v

def default(conf):
	default = conf.pop("default")

	# default setup
	for k, v in default.items():
		conf["setup"].setdefault(k, v)

	# mark default type
	if "mark" in conf:
		for item in conf["mark"]:
			item.setdefault("type", "field")

	return conf

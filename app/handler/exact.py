import collections

def exact(state):
	exa = state["tmp"]["analysis"]["exact"]

	exac = {
		key : [ state["rank"][i] for i in val & exa ]
		for key, val in state["tmp"]["analysis"]["keys"].items()
		if val & exa
	}

	for item in state["tmp"]["items"]:
		item.setdefault("rank", 0)

		item_keys = set(item.keys())
		exac_keys = set(exac.keys())
		keys = item_keys & exac_keys

		for key in keys:
			val = item[key]
			ruls = exac[key]

			for rule in ruls:
				item["rank"] += _rank(val, rule)

def _rank(val, rule):
	if "rank" not in rule or "val" not in rule:
		return 0

	if isinstance(val, dict):
		return sum([ _rank(val, rule) for val in val.values() ])

	if isinstance(val, collections.Iterable):
		return sum([ _rank(val, rule) for val in val ])

	return rule["rank"] if val in rule["val"] else 0

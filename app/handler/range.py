import collections

def range(state):
	ran = state["tmp"]["analysis"]["range"]

	rang = {
		key : [ state["rank"][i] for i in val & ran ]
		for key, val in state["tmp"]["analysis"]["keys"].items()
		if val & ran
	}

	for item in state["tmp"]["items"]:
		item.setdefault("rank", 0)

		item_keys = set(item.keys())
		rang_keys = set(rang.keys())
		keys = item_keys & rang_keys

		for key in keys:
			val = item[key]
			ruls = rang[key]

			for rule in ruls:
				item["rank"] += _rank(val, rule)

def _rank(val, rule):
	if "rank" not in rule:
		return 0

	if isinstance(val, dict):
		return sum([ _rank(val, rule) for val in val.values() ])

	if isinstance(val, collections.Iterable):
		return sum([ _rank(val, rule) for val in val ])

	if "from" in rule and "to" in rule:
		return rule["rank"] if rule["from"] < val < rule["to"] else 0

	if "from" in rule:
		return rule["rank"] if rule["from"] < val else 0

	if "to" in rule:
		return rule["rank"] if val < rule["to"] else 0

	return 0

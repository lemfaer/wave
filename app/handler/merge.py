def merge(state):
	if "old" not in state["tmp"] or "items" not in state["tmp"]:
		return

	if not state["tmp"]["old"] or not state["tmp"]["items"]:
		return

	new = state["tmp"]["items"]
	old = state["tmp"].pop("old")
	old = rank(old)

	for item in new:
		item["rank"] += old[item["id"]]

def rank(items):
	return { item["id"] : item["rank"] for item in items }

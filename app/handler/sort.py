def sort(state):
	if not state["setup"]["sort"]:
		return

	if "items" not in state["tmp"] or not state["tmp"]["items"]:
		return

	if state["setup"]["sort"] == "rank":
		state["tmp"]["items"] = sorted(
			state["tmp"]["items"],
			key = lambda item: item["rank"],
			reverse = True
		)

	if state["setup"]["sort"] == "avg":
		avg = _avg(state["tmp"]["items"])
		state["tmp"]["items"] = sorted(
			state["tmp"]["items"],
			key = lambda item: abs(item["rank"] - avg)
		)

def _avg(items):
	return sum([ item["rank"] for item in items ]) / len(items)

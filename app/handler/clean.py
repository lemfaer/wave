def clean(state):
	if state["tmp"]["items"] is state["tmp"]["_items"]:
		state["tmp"].pop("_items")

	state["tmp"]["items"] = [
		{ key : val for key, val in item.items() if key in ("id", "rank") }
		for item in state["tmp"]["items"]
	]

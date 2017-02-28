def clean(state):
	state["tmp"]["items"] = [
		{ key : val for key, val in item.items() if key in ("id", "rank") }
		for item in state["tmp"]["items"]
	]

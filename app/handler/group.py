def group(state):
	state["tmp"]["old"] = state["tmp"].pop("items", None)
	state["tmp"]["items"] = []

	for response in state["tmp"]["response"]:
		state["tmp"]["items"].extend(response["items"])

	for item in state["tmp"]["items"]:
		item["groups"] = item.pop("items", [])

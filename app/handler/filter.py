_filter = filter

def filter(state):
	state["tmp"]["items"] = _filter(lambda item: item["rank"] > 0, state["tmp"]["items"])

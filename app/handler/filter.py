_filter = filter

def filter(state):
	filt = lambda item: item["rank"] > 0
	item = _filter(filt, state["tmp"]["items"])
	state["tmp"]["items"] = list(item)

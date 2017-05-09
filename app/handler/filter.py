_filter = filter

def filter(state):
	filt = lambda item: item["rank"] > state["setup"]["min"]
	item = _filter(filt, state["tmp"]["items"])
	state["tmp"]["items"] = list(item)

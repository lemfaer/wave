from app.request.next import repeat

def search(state):
	if state["tmp"]["month"] < 12:
		state["tmp"]["items"] = []
		repeat(state)
	else:
		state["tmp"]["items"] = state["tmp"]["_items"]

	for item in state["tmp"]["response"]["items"]:
		item["relation"] = item.pop("relation", None)
		item["followers"] = item.pop("followers_count", None)

		item.setdefault("last_seen", {})
		item["time"] = item["last_seen"].pop("time", None)
		item["platfrorm"] = item["last_seen"].pop("platfrorm", None)
		item.pop("last_seen")

		item.setdefault("personal", {})
		item["life"] = item["personal"].pop("life_main", None)
		item["people"] = item["personal"].pop("people_main", None)
		item["smoking"] = item["personal"].pop("smoking", None)
		item["alcohol"] = item["personal"].pop("alcohol", None)
		item["political"] = item["personal"].pop("political", None)
		item.pop("personal")

	state["tmp"].setdefault("_items", [])
	state["tmp"]["_items"].extend(state["tmp"]["response"]["items"])

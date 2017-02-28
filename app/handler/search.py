def search(state):
	state["tmp"]["old"] = state["tmp"].pop("items", None)
	state["tmp"]["items"] = []

	for response in state["tmp"]["response"]:
		state["tmp"]["items"].extend(response["items"])

	for item in state["tmp"]["items"]:
		item["relation"] = item.pop("relation", 0)
		item["followers"] = item.pop("followers_count", 0)

		item.setdefault("last_seen", {})
		item["time"] = item["last_seen"].pop("time", 0)
		item["platfrorm"] = item["last_seen"].pop("platfrorm", 0)
		item.pop("last_seen")

		item.setdefault("personal", {})
		item["life"] = item["personal"].pop("life_main", 0)
		item["people"] = item["personal"].pop("people_main", 0)
		item["smoking"] = item["personal"].pop("smoking", 0)
		item["alcohol"] = item["personal"].pop("alcohol", 0)
		item["political"] = item["personal"].pop("political", 0)
		item.pop("personal")

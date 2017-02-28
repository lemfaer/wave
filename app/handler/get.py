def get(state):
	state["tmp"]["old"] = state["tmp"].pop("items", None)
	state["tmp"]["items"] = []

	for response in state["tmp"]["response"]:
		state["tmp"]["items"].extend([ item.pop() for item in response ])

	for item in state["tmp"]["items"]:
		item.setdefault("counters", {})
		item["notes_count"] = item["counters"].pop("notes", 0)
		item["pages_count"] = item["counters"].pop("pages", 0)
		item["albums_count"] = item["counters"].pop("albums", 0)
		item["videos_count"] = item["counters"].pop("videos", 0)
		item["audios_count"] = item["counters"].pop("audios", 0)
		item["photos_count"] = item["counters"].pop("photos", 0)
		item["groups_count"] = item["counters"].pop("groups", 0)
		item["friends_count"] = item["counters"].pop("friends", 0)
		item["followers_count"] = item["counters"].pop("followers", 0)
		item["user_videos_count"] = item["counters"].pop("user_videos", 0)
		item["mutual_friends_count"] = item["counters"].pop("mutual_friends", 0)
		item["online_friends_count"] = item["counters"].pop("online_friends", 0)
		item.pop("counters")

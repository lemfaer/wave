from .multi import MultiRequest

class UserSearch(MultiRequest):

	def params(self):
		return [{
			**super(UserSearch, self).params(),
			**self.setup(),
			**self.fields(),
			"birth_month" : month,
			"count" : 1000
		} for month in range(1, 12 + 1)]

	def setup(self):
		setup = self.state["setup"]
		params = {}

		if setup["query"]:
			params["q"] = setup["query"]

		if setup["city"]:
			params["city"] = setup["city"]

		if setup["sex"]:
			params["sex"] = setup["sex"]

		if setup["age"]:
			params["age_from"] = setup["age"]["from"]
			params["age_to"] = setup["age"]["to"]

		return params

	def fields(self):
		keys = self.state["tmp"]["analysis"]["keys"]
		fields = []

		if "relation" in keys:
			fields.append("relation")

		if "followers" in keys:
			fields.append("followers_count")

		if "time" in keys or "platform" in keys:
			fields.append("last_seen")

		for personal in "political", "people", "life", "smoking", "alcohol":
			if personal in keys:
				fields.append("personal")
				break

		return { "fields" : ",".join(fields) }

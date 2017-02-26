import json
from .abstract import AbstractRequest

class UserSearch(AbstractRequest):

	def params(self):
		tmp = self.state["tmp"]
		tmp.setdefault("month", 0)
		tmp["month"] += 1

		return {
			**super().params(),
			**self.setup(),
			**self.fields(),
			"birth_month" : tmp["month"],
			"count" : 1000
		}

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

		for personal in "political", "people", "life", "smoking", "alcohol":
			if personal in keys:
				fields.append("personal")
				break

		return { "fields" : ",".join(fields) }

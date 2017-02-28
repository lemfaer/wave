from .multi import MultiRequest
from math import ceil
import json

class UserGet(MultiRequest):

	def __init__(self, state):
		super(UserGet, self).__init__(state, async = False)

	def need(self):
		return bool(
			"items" in self.state["tmp"]
			and self.state["tmp"]["items"]
			and self.fields()
		)

	def params(self):
		return self.execute([ item["id"] for item in self.state["tmp"]["items"] ], {
			**super(UserGet, self).params(),
			**self.fields()
		})

	def fields(self):
		keys = self.state["tmp"]["analysis"]["keys"]

		counts = [
			"albums_count",
			"videos_count",
			"audios_count",
			"photos_count",
			"notes_count",
			"friends_count",
			"groups_count",
			"online_friends_count",
			"mutual_friends_count",
			"user_videos_count",
			"followers_count",
			"pages_count"
		]

		for count in counts:
			if count in keys:
				return { "fields" : "counters" }

		return {}

	def execute(self, users, params):
		def chunk(l, n):
			for i in range(0, len(l), n):
				yield l[i:i + n]

		with open(self.state["app"]["js"]["get"], "r") as js:
			script = js.read()

		scripts = []
		for users in chunk(users, self.state["app"]["execute"]):
			scripts.append(script.format(
				pyhton_users = json.dumps(users),
				python_params = json.dumps(params)
			))

		return [{ **super(UserGet, self).params(), "code" : script }
			for script in scripts]

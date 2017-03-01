from .multi import MultiRequest
import json

class GroupGet(MultiRequest):

	def __init__(self, state):
		super(GroupGet, self).__init__(state, async = False)

	def need(self):
		return bool(
			"items" in self.state["tmp"]
			and self.state["tmp"]["items"]
			and "groups" in self.state["tmp"]["analysis"]["keys"]
		)

	def params(self):
		return self.execute(
			[ item["id"] for item in self.state["tmp"]["items"] ],
			{ **super(GroupGet, self).params() }
		)

	def execute(self, users, params):
		def chunk(l, n):
			for i in range(0, len(l), n):
				yield l[i:i + n]

		with open(self.state["app"]["js"]["group"], "r") as js:
			script = js.read()

		scripts = []
		for users in chunk(users, self.state["app"]["execute"]):
			scripts.append(script.format(
				pyhton_users = json.dumps(users),
				python_params = json.dumps(params)
			))

		return [{ **super(GroupGet, self).params(), "code" : script }
			for script in scripts]

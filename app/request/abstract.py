import requests, json

class AbstractRequest:

	def __init__(self, state):
		self.state = state

	def send(self):
		root = self.state["app"]["root"]
		method = self.state["app"]["method"][type(self)]
		url = root + method

		res = requests.post(url, params = self.params())
		res = res.text

		self.log(res)
		self.apply(res)

		return self.state

	def params(self):
		return {
			"access_token" : self.state["access"],
			"v" : 5.8
		}

	def log(self, res):
		self.state["tmp"].setdefault("log", [])
		self.state["tmp"]["log"].append(res);

	def apply(self, res):
		self.state["tmp"]["response"] = json.loads(res)["response"]

		# update state
		for handler in self.state["app"]["handlers"][type(self)]:
			handler(self.state)

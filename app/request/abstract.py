import requests, json, urllib.parse
from app.conf import update

class AbstractRequest:

	def __init__(self, state):
		self.state = state

	def url(self):
		url = "{root}{method}?{params}"

		root = self.state["app"]["root"]
		method = self.state["app"]["method"][type(self)]
		params = urllib.parse.urlencode(self.params())

		return url.format(root=root, method=method, params=params)

	def params(self):
		return {
			"access_token" : self.state["access"],
			"v" : 5.8
		}

	def send(self):
		url = self.url()
		res = requests.get(url)

		self.log(res)
		self.apply(res)

		return self.state

	def log(self, res):
		self.state["tmp"].setdefault("log", [])
		self.state["tmp"]["log"].append(res.text);

	def apply(self, res):
		self.state["tmp"]["response"] = json.loads(res.text)["response"]

		# update state
		for handler in self.state["app"]["handlers"][type(self)]:
			handler(self.state)

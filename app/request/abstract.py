import requests
import urllib.parse

class AbstractRequest:

	def __init__(self, state):
		self.state = state

	def url(self):
		url = "{root}{method}?{params}"

		root = self.state["root"]
		method = self.state["method"][type(self)]
		params = urllib.parse.urlencode(self.params())

		return url.format(root=root, method=method, params=params)

	def params(self):
		raise NotImplementedError()

	def send(self):
		return self.apply(requests.get(self.url()))

	def apply(self, responce):
		for handler in self.state["handlers"][type(self)]:
			responce = handler(responce)

		return self.state.update(responce) or self.state

import grequests, json
from math import ceil
from .abstract import AbstractRequest

class MultiRequest(AbstractRequest):

	def __init__(self, state, async = True):
		super().__init__(state)
		self.async = async

	def send(self):
		root = self.state["app"]["root"]
		method = self.state["app"]["method"][type(self)]
		url = root + method

		# chunk requests
		reqss = {}
		for i, params in enumerate(self.params()):
			per = self.state["app"]["async"] if self.async else 1
			rei = ceil((i + 1) / per)

			req = grequests.post(url, params = params)
			reqss.setdefault(rei, [])
			reqss[rei].append(req)

		reqss = list(reqss.values())

		# send all
		resss = []
		for reqs in reqss:
			ress = grequests.map(reqs)
			resss.append(ress)

		# merge responses
		res = self.merge(resss)

		# log and apply
		self.log(res)
		self.apply(res)

		return self.state

	def merge(self, resss):
		return json.dumps({"response" : [
			json.loads(res.text)["response"]
			for ress in resss
			for res in ress
		]})

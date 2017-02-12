from .abstract import AbstractRequest

class CountryGet(AbstractRequest):

	def params(self):
		return { "code" : self.state["setup"]["country"] }

from .abstract import AbstractRequest

class CountryGet(AbstractRequest):

	def need(self):
		return bool(self.state["setup"]["country"])

	def params(self):
		return {
			**super().params(),
			"code" : self.state["setup"]["country"]
		}

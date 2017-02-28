from .abstract import AbstractRequest

class CityGet(AbstractRequest):

	def need(self):
		return bool(self.state["setup"]["country"] and self.state["setup"]["city"])

	def params(self):
		return {
			**super().params(),
			"q" : self.state["setup"]["city"],
			"country_id" : self.state["setup"]["country"]
		}

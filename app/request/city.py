from .abstract import AbstractRequest

class CityGet(AbstractRequest):

	def params(self):
		return {
			**super().params(),
			"q" : self.state["setup"]["city"],
			"country_id" : self.state["setup"]["country"]
		}

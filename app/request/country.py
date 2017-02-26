from .abstract import AbstractRequest

class CountryGet(AbstractRequest):

	def params(self):
		return {
			**super().params(),
			"code" : self.state["setup"]["country"]
		}

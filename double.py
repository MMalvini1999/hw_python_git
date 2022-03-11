def doubler(RandomFunc):
	def function():
		RandomFunc()
		RandomFunc()
	return function


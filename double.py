def doubler(RandomFunc):
	def function():
		RandomFunc()
		RandomFunc()
	return function
def Hello():
	print("Hello ")

Hello=doubler(Hello)
Hello()

def printNum(x):
	print(x)
printNum2=doubler(printNum)
printNum2()

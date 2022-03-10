import time
def calculate_time(timedFunction):
	def function():
		initial_time = time.time()
		timedFunction()
		final_time = time.time()
		execution_time = final_time - initial_time
		print('Total time ', execution_time)
	return function



import time
def calculate_time(timedFunction):
	def function():
		initial_time = time.time()
		timedFunction()
		final_time = time.time()
		execution_time = final_time - initial_time
		print('Total time:', execution_time)
	return function
def timingFunc():
	x=0
	while x < 5:
		x=x+1
timingFunc = calculate_time(timingFunc)
timingFunc()

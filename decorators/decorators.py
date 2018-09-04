#Create decorator
def new_decorator(original_fun):

	def wrap_fun():
		print('This is a sample code, before')
		original_fun()
		print('This is a sample code, after')

	return wrap_fun

#funtion to be decorated
def fun_to_be_decorated():
	print('I need to be decorated')

@new_decorator
def fun_to_be_decorated2():
	print('I need to be decorated')

#example calls
fun_to_be_decorated()

dec_fun = new_decorator(fun_to_be_decorated)
dec_fun()

fun_to_be_decorated2()
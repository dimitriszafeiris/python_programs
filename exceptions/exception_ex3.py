#example 1: try - except - else block until True
def ask():

	while True:
		try:
			n = int(input("Give an integer:"))
		except:
			print("Please try again!")
			continue
		else:
			break

	print("Your integer is:")
	print(n)
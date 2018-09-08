#Find the argument
def find_the_argument(arg):
    if type(arg) == int:
        print (abs(arg))
        print ("You have given an int.")
        return 0
    elif type(arg) == float:
        print (abs(arg))
        print ("You have given a flaot.")
    else:
        print (n)
        print ("You have not given a numeric.")
        return 0

n=input("Give an argument...")
print (type(n))
find_the_argument(n)
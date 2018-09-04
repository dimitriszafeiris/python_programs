#generator of squares up to N
def gensquares(N):
	for i in range(N):
		yield i**2

for x in gensquares(10):
	print(x)

#generator of random number between 1 and 10
import random
random.randint(1,10)

def rand_low_high(low,high,n):
	for i in range(n):
		yield random.randint(low,high)

for num in rand_low_high(1,10,12):
	print(num)

#iterators - convert string to iterator
s = 'This is a string!'
s = iter(s)
print(next(s))
print(next(s))
print(next(s))
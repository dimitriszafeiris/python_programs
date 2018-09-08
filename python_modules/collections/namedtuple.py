from collections import namedtuple

Dog = namedtuple('Dog','age breed name')

sam = Dog(age=5,breed='Lab',name='Sam')
sam

sam.age
sam[0]

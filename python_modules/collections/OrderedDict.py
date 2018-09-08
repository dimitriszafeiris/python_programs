from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
	print k,v

#compare Ordered Dictionaries
d1 = OrderedDict()
d1['a'] = 1 
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print d1 == d2 # returns False (True at normal dictionaries)

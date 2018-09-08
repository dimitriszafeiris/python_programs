from collections import defaultdict

d = defaultdict(object)
d['one']

for item in d:
	print item

d = defaultdict(lambda : 0)
d['one']

d['two'] = 2
d
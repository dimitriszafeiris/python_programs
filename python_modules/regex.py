import re

patterns = ['term1','term2']
text = 'This text contains term1, but not the other word.'

for pattern in patterns:
	print('Searching for %s in:%s' % (pattern,text))

	if re.search(pattern,text):
		print ('Match found.')
	else:
		print ('Match not found.')
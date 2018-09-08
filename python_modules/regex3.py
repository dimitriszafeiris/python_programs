import re

def multi_re_find(patterns,phrase):

	for pattern in patterns:
		print ('Searching the phrase usring the re check: %r %pattern')
		print (re.findall(pattern,phrase))
		pint ('\n')

test_phase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['sd*', #s followed by 0 or more d
				'sd+', #s followed by 1 or mode d
				'sd?', # s followed by 0 or 1 d
				'sd{3},' #s followed by 3 d
				'sd{2,3}' #s followed by 2 to 3 d
				]

multi_re_find(test_patterns,test_phase)

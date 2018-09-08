#counter 
from collections import Counter

l = [1,1,1,2,3,1,4,5,6,7,8,9,11,12,15]
Counter(l)

s = 'aaashshsdhsdgkbaksfb'
Counter(s)

s = 'How many times does each word show up up up here here times'
words = s.split()
Counter(words)

c = Counter(words)
c.most_common(2) # 2 most common words

sum(c.values())

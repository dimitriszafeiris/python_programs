#Add postfix at a name
postfix = 'end'

original = input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word + first + postfix
new_word = new_word[1:len(new_word)]
#print (new_word[1:len(new_word)])
if len(new_word) > 0 and new_word.isalpha():
    print (new_word)
else:
    print ('Wrong input!')
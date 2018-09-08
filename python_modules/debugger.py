#debugger module
import pdb

x = [1,2,3]
y =2
z =3

result = y+z
print result

pdb.set_trace() # debugger starts here, exit with 'q'

result2 = y+x # Error, adding an integer to a list
print result2
import StringIO

message = 'This is a message'

f = StringIO.StringIO(message)

f.read()
f.write('This is the second line')

f.seek(0)
f.read()
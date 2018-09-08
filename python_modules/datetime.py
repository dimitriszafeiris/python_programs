import datetime

t = datetime.time(5,30,1)
print t

print datetime.time.min
print datetime.time.max
print datetime.time.resolution

today = datetime.date.today()
print today

today.timetuple()
today.day

print datetime.date.min
print datetime.date.max
print datetime.date.resolution

d1 = datetime.date(2018,9,9)
print d1

d2 = d1.replace(year=2019)
d1 - d2 # difference in days
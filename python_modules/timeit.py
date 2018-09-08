import timeit

#calculate time of below commands
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

timeit.timeit('"-".join(map(str,range(100)))', number=10000)


import timeit
import numpy as np
# r number of runs, n number of loops
# This things is only for iPython
# %%timeit -r2 -n10

starttime = timeit.default_timer()
print("The start time is :",starttime)
def test():
    return range(1001)
def test2():
    return [x for x in range(1001)]
test()
print("The time difference is :", timeit.default_timer() - starttime)

starttime2 = timeit.default_timer()
test2()
print("The time 2 difference is :", timeit.default_timer() - starttime2)
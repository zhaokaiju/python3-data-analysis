# IPython log file

print(data)
import numpy as np
from numpy.random import randn
data = {i:randn() for i in range(7)}
data
print(data)
an_apple = 29
import datetime
datetime.MAXYEAR
get_ipython().magic('pinfo b')
get_ipython().magic('pinfo an_apple')
def add_numbers(a, b):
    return a + b
get_ipython().magic('pinfo add_numbers')
get_ipython().magic('pinfo2 add_numbers')
get_ipython().magic('pinfo add_numbers')
get_ipython().magic('pinfo add_numbers')
# 显示该函数的源代码
get_ipython().magic('pinfo2 add_numbers')
a = np.random.randn(100, 100)
get_ipython().magic('timeit np.dot(a, a)')
get_ipython().magic('hist')
ipython --pylab
--pylab
2 ** 3
_
get_ipython().magic('logstart')
get_ipython().magic('logstop')

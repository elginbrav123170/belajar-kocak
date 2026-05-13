# Python3 code to demonstrate working of
# Unique elements in nested tuple
# Using nested loop + set()

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list 
print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using nested loop + set()
res = []
temp = set()
for inner in test_list:
        for ele in inner:
            if not ele in temp:
                temp.add(ele)
                res.append(ele)

# printing result
print("Unique elements in nested tuples are : " + str(res))

# Python3 code to demonstrate working of
# Unique elements in nested tuple
# Using from_iterable() + set()
from itertools import chain

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list 
print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using from_iterable() + set()
res = list(set(chain.from_iterable(test_list)))

# printing result
print("Unique elements in nested tuples are : " + str(res))

# Python3 code to demonstrate working of
# Unique elements in nested tuple

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list
print("The original list : " + str(test_list))

# Unique elements in nested tuple
x=[]
for i in test_list:
    i=list(i)
    x.extend(i)
res=list(set(x))
# printing result
print("Unique elements in nested tuples are : " + str(res))

# Python3 code to demonstrate working of
# Unique elements in nested tuple
from collections import Counter
# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list
print("The original list : " + str(test_list))

# Unique elements in nested tuple
x = []
for i in test_list:
    x.extend(list(i))
freq = Counter(x)
res = list(freq.keys())
res.sort()
# printing result
print("Unique elements in nested tuples are : " + str(res))

# Python3 code to demonstrate working of
# Unique elements in nested tuple

import operator as op
# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list 
print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using nested loop + set()
res = []
temp = set()
for inner in test_list:
        for ele in inner:
            if op.countOf(temp,ele)==0:
                temp.add(ele)
                res.append(ele)
res.sort()
# printing result
print("Unique elements in nested tuples are : " + str(res))

# Python3 code to demonstrate working of
# Unique elements in nested tuple

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list 
print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using list comprehension and set conversion
res = sorted(set([x for inner in test_list for x in inner]))

# printing result
print("Unique elements in nested tuples are : " + str(res))

# Python3 code to demonstrate working of
# Unique elements in nested tuple

# import numpy module
import numpy as np

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list
print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using numpy.unique() function
res = np.unique(np.concatenate(test_list)).tolist()

# printing result
print("Unique elements in nested tuples are : " + str(res))
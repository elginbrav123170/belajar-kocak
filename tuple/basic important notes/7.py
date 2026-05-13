# Python3 code to demonstrate working of
# Tuple modulo
# using zip() + generator expression

# Initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# Printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo
# using zip() + generator expression
res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2))

# Printing result
print("The modulus tuple : " + str(res))

# Python3 code to demonstrate working of
# Tuple modulo
# using map() + mod
from operator import mod

# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo
# using map() + mod
res = tuple(map(mod, test_tup1, test_tup2))

# printing result
print("The modulus tuple : " + str(res))

# Python3 code to demonstrate working of
# Tuple modulo

# Initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# Printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo
res=[]
for i in range(0,len(test_tup1)):
    res.append(test_tup1[i]%test_tup2[i])
res=tuple(res)

# Printing result
print("The modulus tuple : " + str(res))

import numpy as np

# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo using numpy
res = tuple(np.mod(test_tup1, test_tup2))

# printing result
print("The modulus tuple : " + str(res))

#This code is contributed by Edula Vinay Kumar Reddy

# Python3 code to demonstrate working of
# Tuple modulo
# using recursive method
def modulo_tuple(t1, t2, result=()):
    if not t1:
        return result
    return modulo_tuple(t1[1:], t2[1:], result + (t1[0] % t2[0],))


# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo
result = modulo_tuple(test_tup1, test_tup2)

# printing result
print("The modulus tuple : " + str(result))

# this code contributed by tvsk

import itertools

# Initializing list
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# Printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

result = tuple(itertools.starmap(lambda x, y: x %
                                 y, zip(test_tup1, test_tup2)))

# Printing the result 
print("The modulus tuple : " + str(result))

# This code is contributed by Jyothi pinjala.

import heapq

test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

modulus_tup = tuple(heapq.nlargest(len(test_tup1), (x % y for x, y in zip(test_tup1, test_tup2))))

print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
print("The modulus tuple : " + str(modulus_tup))
#This code is contributed by Rayudu.

# Python3 code to demonstrate working of
# Tuple modulo
# using List comprehension

# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo
# using List comprehension
res = [ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)]
res = tuple(res)

# printing result
print("The modulus tuple : " + str(res))
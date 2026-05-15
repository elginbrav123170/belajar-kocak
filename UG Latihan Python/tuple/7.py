# Python3 code to demonstrate working of
# Concatenating tuples to nested tuples
# using + operator + ", " operator during initialization

# initialize tuples
test_tup1 = (3, 4),
test_tup2 = (5, 6),

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Concatenating tuples to nested tuples
# using + operator + ", " operator during initialization
res = test_tup1 + test_tup2

# printing result
print("Tuples after Concatenating : " + str(res))

# Python3 code to demonstrate working of
# Concatenating tuples to nested tuples
# Using ", " operator during concatenation

# initialize tuples
test_tup1 = (3, 4)
test_tup2 = (5, 6)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Concatenating tuples to nested tuples
# Using ", " operator during concatenation
res = ((test_tup1, ) + (test_tup2, ))

# printing result
print("Tuples after Concatenating : " + str(res))

# Python3 code to demonstrate working of
# Concatenating tuples to nested tuples
# using + operator + ", " operator during initialization

# initialize tuples
test_tup1 = (3, 4),
test_tup2 = (5, 6),

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Concatenating tuples to nested tuples
test_tup1 = list(test_tup1)
test_tup2 = list(test_tup2)
test_tup1.extend(test_tup2)
# printing result
print("Tuples after Concatenating : " + str(tuple(test_tup1)))

import itertools

test_tup1 = (3, 4),
test_tup2 = (5, 6),

# using itertools.chain() to concatenate tuples to nested tuples
res = tuple(itertools.chain(test_tup1, test_tup2))

# printing result
print("Tuples after Concatenating : ", res)

# Python3 code to demonstrate working of
# Concatenating tuples to nested tuples
# using functools.reduce() method

# import functools module
import functools

# initialize tuples
test_tup1 = (3, 4),
test_tup2 = (5, 6),

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Concatenating tuples to nested tuples
# using functools.reduce() method
res = functools.reduce(lambda x, y: x + y, (test_tup1, test_tup2))

# printing result
print("Tuples after Concatenating : " + str(res))

# Python3 code to demonstrate working of
# Concatenating tuples to nested tuples
# using extend() method of list class

# initialize tuples
test_tup1 = (3, 4)
test_tup2 = (5, 6)

# create an empty list
lst = []

# Concatenating tuples to nested tuples
# using extend() method of list class
lst.extend(test_tup1)
lst.extend(test_tup2)
res = tuple([lst[i:i+2] for i in range(0, len(lst), 2)])

# printing result
print("Tuples after Concatenating : ", res)
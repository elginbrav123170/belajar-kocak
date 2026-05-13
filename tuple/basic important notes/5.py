def summation(test_tup):

    # Converting into list
    test = list(test_tup)

    # Initializing count
    count = 0

    # for loop
    for i in test:
        count += i
    return count


# Initializing test_tup
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))

# Python 3 code to demonstrate working of
# Tuple elements inversions
# Using map() + list() + sum()

# initializing tup
test_tup = ([7, 8], [9, 1], [10, 7])

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using map() + list() + sum()
res = sum(list(map(sum, list(test_tup))))

# printing result
print("The summation of tuple elements are : " + str(res))

# Python3 code to demonstrate working of
# Tuple summation

# Initializing tuple
test_tup = (7, 8, 9, 1, 10, 7)

# Printing original tuple
print("The original tuple is : " + str(test_tup))

res = 0
for i in test_tup:
    res += i

# Printing result
print("The summation of tuple elements are : " + str(res))

def summation(test_tup):
    # Convert the tuple to a list using a list comprehension
    test = [x for x in test_tup]
    
    # Find the sum of the elements in the list using the built-in sum() function
    return sum(test)

# Test the function with a tuple of integers
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))

def summation2(test_tup):
    # Check if the input is empty or contains non-integer elements
    if len(test_tup) == 0:
        raise ValueError("Input tuple is empty")
    if not all(isinstance(x, int) for x in test_tup):
        raise TypeError("Input tuple must contain only integers")
    
    # Use a generator expression to convert 
    # the tuple to an iterable
    iterable = (x for x in test_tup)
    
    # Find the sum of the elements in the iterable 
    # using the built-in sum() function
    total_sum = sum(iterable)
    
    return total_sum
test_tup = (5, 20, 3, 7, 6, 8)
print(summation2(test_tup))

import math

# initializing tuple
test_tup = (7, 8, 9, 1, 10, 7)

# calculating sum of tuple elements using math.fsum()
res = math.fsum(test_tup)

# printing result
print("The summation of tuple elements are : " + str(res))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

combined = zip(tuple1, tuple2, tuple3)
result = tuple(map(sum, combined))
print(result)

import operator
from functools import reduce

def summation(test_tup):
# Using reduce() + operator.add()
  return reduce(operator.add, test_tup)

#initializing test_tup
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))
#This code is contributed by Edula Vinay Kumar Reddy

# Python3 code to demonstrate working of
# Tuple summation using numpy
import numpy as np

# Initializing tuple
test_tup = (7, 8, 9, 1, 10, 7)

# Converting tuple to numpy array
test_array = np.array(test_tup)

# Printing original tuple
print("The original tuple is : " + str(test_tup))

# Finding sum of array elements
res = np.sum(test_array)

# Printing result
print("The summation of tuple elements are : " + str(res))
# Python3 code to demonstrate working of 
# Elementwise AND in tuples
# using zip() + generator expression 

# initialize tuples 
test_tup1 = (10, 4, 6, 9) 
test_tup2 = (5, 2, 3, 3) 

# printing original tuples 
print(&quot;The original tuple 1 : &quot; + str(test_tup1)) 
print(&quot;The original tuple 2 : &quot; + str(test_tup2)) 

# Elementwise AND in tuples
# using zip() + generator expression 
res = tuple(ele1 &amp; ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 

# printing result 
print(&quot;The AND tuple : &quot; + str(res))

# Python3 code to demonstrate working of 
# Elementwise AND in tuples 
# using map() + iand 
from operator import iand 

# initialize tuples 
test_tup1 = (10, 4, 6, 9) 
test_tup2 = (5, 2, 3, 3) 

# printing original tuples 
print(&quot;The original tuple 1 : &quot; + str(test_tup1)) 
print(&quot;The original tuple 2 : &quot; + str(test_tup2)) 

# Elementwise AND in tuples 
# using map() + iand
res = tuple(map(iand, test_tup1, test_tup2)) 

# printing result 
print(&quot;The AND tuple : &quot; + str(res))

# Python3 code to demonstrate working of
# Elementwise AND in tuples
# using numpy.bitwise_and

import numpy as np

# initialize tuples
test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Elementwise AND in tuples
# using numpy.bitwise_and
res = tuple(np.bitwise_and(np.array(test_tup1), np.array(test_tup2)))

# printing result
print("The AND tuple : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy

# Initialize input tuples
test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# Perform elementwise AND operation using a list comprehension and bitwise &
res = tuple(test_tup1[i] & test_tup2[i] for i in range(len(test_tup1)))

# Print the resulting tuple
print("The AND tuple: " + str(res))

test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

and_tuple = ()
for i in range(len(test_tup1)):
    and_tuple += ((test_tup1[i] & test_tup2[i]),)

print("The AND tuple:", and_tuple)
# Python3 code to demonstrate working of 
# Tuple XOR operation
# using zip() + generator expression 

# initialize tuples 
test_tup1 = (10, 4, 6, 9) 
test_tup2 = (5, 2, 3, 3) 

# printing original tuples 
print(&quot;The original tuple 1 : &quot; + str(test_tup1)) 
print(&quot;The original tuple 2 : &quot; + str(test_tup2)) 

# Tuple XOR operation
# using zip() + generator expression 
res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 

# printing result 
print(&quot;The XOR tuple : &quot; + str(res))

# Python3 code to demonstrate working of 
# Tuple XOR operation 
# using map() + xor
from operator import xor

# initialize tuples 
test_tup1 = (10, 4, 6, 9) 
test_tup2 = (5, 2, 3, 3) 

# printing original tuples 
print(&quot;The original tuple 1 : &quot; + str(test_tup1)) 
print(&quot;The original tuple 2 : &quot; + str(test_tup2)) 

# Tuple XOR operation 
# using map() + xor
res = tuple(map(xor, test_tup1, test_tup2)) 

# printing result 
print(&quot;The XOR tuple : &quot; + str(res))

# Python3 code to demonstrate working of 
# Tuple XOR operation 
# using numpy 
import numpy as np
  
# initialize tuples 
test_tup1 = (10, 4, 6, 9) 
test_tup2 = (5, 2, 3, 3) 
  
# printing original tuples 
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 
  
# Tuple XOR operation 
# using numpy 
res = np.bitwise_xor(test_tup1,test_tup2)
  
# printing result 
print("The XOR tuple : " + str(tuple(res)))

# Python3 code to demonstrate working of
# Tuple XOR operation

# initialize tuples
test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple XOR operation
res=[]
for i in range(0,len(test_tup1)):
    res.append(test_tup1[i]^test_tup2[i])
res=tuple(res)
# printing result
print("The XOR tuple : " + str(res))

# initialize tuples
test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# perform XOR operation using list comprehension
res = tuple([test_tup1[i] ^ test_tup2[i] for i in range(len(test_tup1))])

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# print the result
print("The XOR tuple : " + str(res))

import operator
import itertools

test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# Tuple XOR operation using itertools.starmap() and operator.xor()
res = tuple(itertools.starmap(operator.xor, zip(test_tup1, test_tup2)))

# printing result
print("The XOR tuple : " + str(res))

import pandas as pd

# initialize tuples 
test_tup1 = (10, 4, 6, 9) 
test_tup2 = (5, 2, 3, 3) 
  
# printing original tuples 
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 

# create pandas DataFrames
df1 = pd.DataFrame(list(test_tup1)).T
df2 = pd.DataFrame(list(test_tup2)).T

# perform XOR operation
res_df = df1.astype(int).apply(lambda x: x^df2.astype(int).iloc[0], axis=1)

# convert result DataFrame to tuple
res = tuple(res_df.iloc[0].tolist())

# print result
print("The XOR tuple : ", res)
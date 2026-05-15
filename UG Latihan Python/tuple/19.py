# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + lambda

# initialize tuples 
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples 
print(&quot;The original tuple 1 : &quot; + str(test_tup1))
print(&quot;The original tuple 2 : &quot; + str(test_tup2))

# Cross Tuple AND operation
# using map() + lambda
res = tuple(map(lambda i, j: i &amp; j, test_tup1, test_tup2))

# printing result
print(&quot;Resultant tuple after AND operation : &quot; + str(res))

# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + iand()
import operator

# initialize tuples 
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples 
print(&quot;The original tuple 1 : &quot; + str(test_tup1))
print(&quot;The original tuple 2 : &quot; + str(test_tup2))

# Cross Tuple AND operation
# using map() + iand()
res = tuple(map(operator.iand, test_tup1, test_tup2))

# printing result
print(&quot;Resultant tuple after AND operation : &quot; + str(res))

# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using List comprehension

# initialize tuples 
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)
  
# printing original tuples 
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
  
# Cross Tuple AND operation
# using List comprehension
res = tuple([i & j for i,j in zip(test_tup1, test_tup2)])
  
# printing result
print("Resultant tuple after AND operation : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy

test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)
# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
res = tuple([i & j for i, j in zip(test_tup1, test_tup2)])
print(res)
#This code is contributed by Jyothi pinjala

def bitwise_and_tuples(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i] & tup2[i])
    return tuple(result)
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)
res = bitwise_and_tuples(test_tup1, test_tup2)
print(res)
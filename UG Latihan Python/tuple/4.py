# Python3 code to demonstrate working of
# Remove nested records
# using isinstance() + enumerate() + loop

# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Remove nested records
# using isinstance() + enumerate() + loop
res = tuple()
for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
        res = res + (ele, )

# printing result
print("Elements after removal of nested records : " + str(res))

# Python3 code to demonstrate working of
# Remove nested records

# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Remove nested records
res=[]
for i in test_tup:
    if not type(i) is tuple:
        res.append(i)
res=tuple(res)
# printing result
print("Elements after removal of nested records : " + str(res))

# Python3 code to demonstrate working of
# Remove nested records

# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Remove nested records
res = list(filter(lambda x: not isinstance(x, tuple), test_tup))

# printing result
print("Elements after removal of nested records : " + str(res))

# Python3 code to demonstrate working of
# Remove nested records
 
# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)
 
# printing original tuple
print("The original tuple : " + str(test_tup))
 
# Remove nested records
res = [x for x in test_tup if not isinstance(x, tuple)]
 
# printing result
print("Elements after removal of nested records : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy

from functools import reduce
test_tup = (1, 5, 7, (4, 6), 10)
# printing original tuple
print("The original tuple : " + str(test_tup))
res = reduce(lambda acc, x: acc + (x,) if not isinstance(x, tuple) else acc, test_tup, ())
print(res)
#This code is contributed by Jyothi pinjala.

def flatten_tuple(tup):
    """
    Recursively flatten a tuple of any depth into a single tuple.

    Args:
        tup: A tuple to be flattened.

    Returns:
        A flattened tuple.

    """
    result = []
    for elem in tup:
        if not isinstance(elem, tuple):
            result.append(elem)
        else:
            result.extend(flatten_tuple(elem))
    return tuple(result)

# Driver code to test the function
test_tup = (1, 5, 7, (4, 6), 10)
print("The original tuple: " + str(test_tup))

# Call the function to flatten the tuple
res = flatten_tuple(test_tup)

# Print the flattened tuple
print(res)
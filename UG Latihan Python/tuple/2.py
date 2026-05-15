# Python3 code to demonstrate working of 
# Extract Symmetric Tuples
# Using dictionary comprehension + set()

# initializing list
test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Extract Symmetric Tuples
# Using dictionary comprehension + set()
temp = set(test_list) & {(b, a) for a, b in test_list}
res = {(a, b) for a, b in temp if a < b}

# printing result 
print("The Symmetric tuples : " + str(res))

# Python3 code to demonstrate working of 
# Extract Symmetric Tuples
# Using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Extract Symmetric Tuples
# Using Counter() + list comprehension<
temp = [(sub[1], sub[0]) if sub[0] < sub[1] else sub for sub in test_list]
cnts = Counter(temp)
res = [key for key, val in cnts.items() if val == 2]

# printing result 
print("The Symmetric tuples : " + str(res))

# Python3 code to demonstrate working of 
# Extract Symmetric Tuples
# Using nested for loops and a temporary set

# initializing list
test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Extract Symmetric Tuples
# Using nested for loops and a temporary set
temp_set = set()
res = []
for tpl in test_list:
    if tpl in temp_set or (tpl[1], tpl[0]) in temp_set:
        res.append(tpl)
    else:
        temp_set.add(tpl)

# printing result 
print("The Symmetric tuples : " + str(res))
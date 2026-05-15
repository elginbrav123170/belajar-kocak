# Python3 code to demonstrate working of 
# Sort Tuples by Maximum element
# Using max() + sort()

# helper function
def get_max(sub):
    return max(sub)

# initializing list
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
print("The original list is : " + str(test_list))

# sort() is used to get sorted result
# reverse for sorting by max - first element's tuples
test_list.sort(key = get_max, reverse = True)

# printing result 
print("Sorted Tuples : " + str(test_list))

# Python3 code to demonstrate working of 
# Sort Tuples by Maximum element
# Using sort() + lambda + reverse

# initializing list
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
print("The original list is : " + str(test_list))

# lambda function getting maximum elements 
# reverse for sorting by max - first element's tuples
test_list.sort(key = lambda sub : max(sub), reverse = True)

# printing result 
print("Sorted Tuples : " + str(test_list))

# initializing list
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
print("The original list is : " + str(test_list))

# using a loop to find the maximum element and sort based on it
sorted_list = []
max_val = 0
for tup in test_list:
    max_val = max(tup)
    sorted_list.append((tup, max_val))
sorted_list.sort(key=lambda x: x[1], reverse=True)
final_list = [tup[0] for tup in sorted_list]

# printing result
print("Sorted Tuples : " + str(final_list))

import heapq

# initializing list
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
print("The original list is : " + str(test_list))

# using heapq to find the maximum element and sort based on it
max_values = []
for tup in test_list:
    max_values.append(heapq.nlargest(1, tup)[0])
new_list = list(zip(test_list, max_values))
sorted_list = sorted(new_list, key=lambda x: x[1], reverse=True)
final_list = [tup[0] for tup in sorted_list]

# printing result
print("Sorted Tuples : " + str(final_list))
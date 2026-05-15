# Python3 code to demonstrate working of 
# Sort by Frequency of second element in Tuple List
# Using sorted() + loop + defaultdict() + lambda
from collections import defaultdict

# initializing list
test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

# constructing mapping
freq_map = defaultdict(int)
for idx, val in test_list:
    freq_map[val] += 1

# performing sort of result 
res = sorted(test_list, key = lambda ele: freq_map[ele[1]], reverse = True)

# printing results
print("Sorted List of tuples : " + str(res))

# Python3 code to demonstrate working of 
# Sort by Frequency of second element in Tuple List
# Using Counter() + lambda + sorted()
from collections import Counter

# initializing list
test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

# constructing mapping using Counter
freq_map = Counter(val for key, val in test_list)

# performing sort of result 
res = sorted(test_list, key = lambda ele: freq_map[ele[1]], reverse = True)

# printing results
print("Sorted List of tuples : " + str(res))

from itertools import groupby  # import groupby function from itertools module

def sort_by_frequency(test_list):  # define function called sort_by_frequency that takes a list called test_list as input
    freq_dict = {val: len(list(group)) for val, group in groupby(sorted(test_list, key=lambda x: x[1]), lambda x: x[1])}  
    # create a dictionary called freq_dict where each key is a unique second element of a tuple in test_list and its value is the number of times that second element appears in test_list
    # we do this by using the groupby function to group the tuples in test_list by their second element, then using len to count the number of tuples in each group
    # we use sorted to sort the list of tuples by their second element before using groupby, and we use a lambda function to specify that we want to group by the second element of each tuple
    # the resulting dictionary has keys that are unique second elements from test_list and values that are the frequency of each second element in test_list
    return sorted(test_list, key=lambda x: freq_dict[x[1]], reverse=True)  
    # sort the original list of tuples (test_list) based on the values in freq_dict
    # we use a lambda function to specify that we want to sort by the value in freq_dict corresponding to the second element of each tuple in test_list
    # we sort the list in reverse order (highest frequency first)
    
test_list = [(6, 5), (1, 7), (2, 5), (8, 7), (9, 8), (3, 7)]  # define test_list
print("The original list is : " + str(test_list))  # print the original list
print("The sorted list is : " + str(sort_by_frequency(test_list)))  # print the sorted list returned by the sort_by_frequency function

import numpy as np

# initializing list
test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

# convert the list to a numpy array
arr = np.array(test_list)

# get the frequency of each second element using numpy's unique function
counts = np.unique(arr[:, 1], return_counts=True)

# sort the indices based on the frequency of the second element using numpy's argsort function
sorted_indices = np.argsort(-counts[1])

# create an empty array to store the sorted tuples
sorted_arr = np.empty_like(arr)

# iterate over the sorted indices and fill in the sorted array
start = 0
for i in sorted_indices:
    freq = counts[1][i]
    indices = np.where(arr[:, 1] == counts[0][i])[0]
    end = start + freq
    sorted_arr[start:end] = arr[indices]
    start = end

# convert the sorted array back to a list of tuples
res = [tuple(row) for row in sorted_arr]

# printing results
print("Sorted List of tuples : " + str(res))
# Python3 code to demonstrate working of 
# Tuple List intersection [ Order irrespective ]
# Using sorted() + set() + & operator + list comprehension

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Using sorted() + set() + & operator + list comprehension
# Using & operator to intersect, sorting before performing intersection
res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])

# printing result 
print("List after intersection : " + str(res))

# Python3 code to demonstrate working of 
# Tuple List intersection [ Order irrespective ]
# Using list comprehension + map() + frozenset() + & operator

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Using list comprehension + map() + frozenset() + & operator
# frozenset used as map() requires hashable container, which 
# set is not, result in frozenset format
res = set(map(frozenset, test_list1)) & set(map(frozenset, test_list2))

# printing result 
print("List after intersection : " + str(res))

# Python3 code to demonstrate working of
# Tuple List intersection [ Order irrespective ]
# Using set() + frozenset() + intersection() + list comprehension

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Using set() + frozenset() + intersection() + list comprehension
set1 = set(frozenset(ele) for ele in test_list1)
set2 = set(frozenset(ele) for ele in test_list2)
res = [tuple(ele) for ele in (set1 & set2)]

# printing result
print("List after intersection : " + str(res))

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# Creating an empty dictionary
freq_dict = {}

# Looping through the tuples in test_list1 and test_list2
for tup in test_list1 + test_list2:
    # Sorting the tuple and converting it to a string
    sorted_tup_str = str(sorted(tup))
    
    # Checking if the string is already in freq_dict
    if sorted_tup_str in freq_dict:
        freq_dict[sorted_tup_str] += 1
    else:
        freq_dict[sorted_tup_str] = 1

# Creating a list comprehension using the tuples that appear in both lists
res = [tup for tup in test_list1 if freq_dict[str(sorted(tup))] >= 2]

# Printing the resulting list
print("List after intersection: " + str(res))

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# Using nested loops
res = []
for tup1 in test_list1:
    for tup2 in test_list2:
        if set(tup1) == set(tup2):
            res.append(tup1)

# printing result
print("List after intersection : " + str(res))
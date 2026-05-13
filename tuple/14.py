# Python3 code to demonstrate working of
# Intersection in Tuple Records Data
# Using list comprehension

# Initializing lists
test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# printing original lists
print(&quot;The original list 1 is : &quot; + str(test_list1))
print(&quot;The original list 2 is : &quot; + str(test_list2))

# Intersection in Tuple Records Data
# Using list comprehension
res = [ele1 for ele1 in test_list1 
       for ele2 in test_list2 if ele1 == ele2]

# printing result
print(&quot;The Intersection of data records is : &quot; + str(res))

# Python3 code to demonstrate working of
# Intersection in Tuple Records Data
# Using set.intersection()

# Initializing lists
test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# printing original lists
print(&quot;The original list 1 is : &quot; + str(test_list1))
print(&quot;The original list 2 is : &quot; + str(test_list2))

# Intersection in Tuple Records Data
# set.intersection()
res = list(set(test_list1).intersection(set(test_list2)))

# printing result
print(&quot;The Intersection of data records is : &quot; + str(res))

# define the two lists of tuples
list1 = [('gfg', 1), ('is', 2), ('best', 3)]
list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# create two dictionaries from the lists
dict1 = dict(list1)
dict2 = dict(list2)

# find the keys that are present in both dictionaries
common_keys = set(dict1.keys()).intersection(set(dict2.keys()))

# create a list of tuples with the common keys and their values
result = [(key, dict1[key]) for key in common_keys]

# print the result
print("The Intersection of data records is :", result)

test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]
# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
 
res = list(filter(lambda t: t in test_list2, test_list1))

print("The Intersection of data records is : " + str(res))
#This code is contributed by Jyothi pinjala

# test data
test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# initialize an empty list
intersection = []

# loop through each tuple in test_list1
for tuple1 in test_list1:
    # extract the first element (string)
    str1 = tuple1[0]
    # loop through each tuple in test_list2
    for tuple2 in test_list2:
        # extract the first element (string)
        str2 = tuple2[0]
        # if the strings match, append the tuple from test_list1 to intersection
        if str1 == str2:
            intersection.append(tuple1)

# print the intersection
print("The intersection of data records is:", intersection)

import itertools

test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# use itertools.product() to create a Cartesian product of the two lists
cartesian_product = list(itertools.product(test_list1, test_list2))

# use list comprehension to filter the resulting list
filtered_list = [x for x in cartesian_product if x[0][0] == x[1][0]]

# use list comprehension to extract the tuples that match the condition in step 3
intersection = [x[0] for x in filtered_list]

# print the intersection
print("The intersection of data records is:", intersection)
# Python3 code to demonstrate working of 
# Filter Tuples by Kth element from List
# Using list comprehension

# initializing list
test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# printing original list
print("The original list is : " + str(test_list))

# initializing check_list
check_list = [4, 2, 8, 10]

# initializing K 
K = 1

# checking for presence on Kth element in list 
# one liner 
res = [sub for sub in test_list if sub[K] in check_list]

# printing result 
print("The filtered tuples : " + str(res))

# Python3 code to demonstrate working of 
# Filter Tuples by Kth element from List
# Using filter() + lambda

# initializing list
test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# printing original list
print("The original list is : " + str(test_list))

# initializing check_list
check_list = [4, 2, 8, 10]

# initializing K 
K = 1

# filter() perform filter, lambda func. checks for presence
# one liner 
res = list(filter(lambda sub: sub[K] in check_list, test_list))

# printing result 
print("The filtered tuples : " + str(res))

# Python3 code to demonstrate working of 
# Filter Tuples by Kth element from List
# Using for loop

# initializing list
test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# printing original list
print("The original list is : " + str(test_list))

# initializing check_list
check_list = [4, 2, 8, 10]

# initializing K 
K = 1

# initializing empty result list
res = []

# iterating over tuples in test_list
for tup in test_list:
    # checking if Kth element is in check_list
    if tup[K] in check_list:
        # appending tuple to result list
        res.append(tup)

# printing result 
print("The filtered tuples : " + str(res))

# Python program for the above approach

# Function to filter tuples
def filter_tuples(test_list, K, check_list):
    if not test_list:
        return []
    if test_list[0][K] in check_list:
        return [test_list[0]] + filter_tuples(test_list[1:], K, check_list)
    else:
        return filter_tuples(test_list[1:], K, check_list)


# initializing list
test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# initializing check_list
check_list = [4, 2, 8, 10]

# initializing K
K = 1

# calling function and storing result in res
res = filter_tuples(test_list, K, check_list)

# printing original list
print("The original list is : " + str(test_list))

# printing result
print("The filtered tuples : " + str(res))
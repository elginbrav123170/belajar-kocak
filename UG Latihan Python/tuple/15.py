# Python3 code to demonstrate working of
# Unique Tuple Frequency [ Order Irrespective ]
# Using tuple() + list comprehension + sorted() + len()

# initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Using tuple() + list comprehension + sorted() + len()
# Size computed after conversion to set
res = len(list(set(tuple(sorted(sub)) for sub in test_list)))

# printing result
print("Unique tuples Frequency : " + str(res))

# Python3 code to demonstrate working of
# Unique Tuple Frequency [ Order Irrespective ]
# Using map() + sorted() + tuple() + set() + len()

# initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Using map() + sorted() + tuple() + set() + len()
# inner map used to perform sort and outer sort to
# convert again in tuple format
res = len(list(set(map(tuple, map(sorted, test_list)))))

# printing result
print("Unique tuples Frequency : " + str(res))

def unique_tuple_frequency(test_list):
  
    # base case
    if len(test_list) == 0:
        return 0

    # recursive call
    rest_freq = unique_tuple_frequency(test_list[1:])

    # check if the first element is unique
    for t in test_list[1:]:
        if sorted(test_list[0]) == sorted(t):
            return rest_freq

    # if the first element is unique, add 1 to the frequency
    return rest_freq + 1


# initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
print("The original list is :" + str(test_list))

# Using map() + sorted() + tuple() + set() + len()
# inner map used to perform sort and outer sort to
# convert again in tuple format
res = unique_tuple_frequency(test_list)

# printing result
print("Unique tuples Frequency : " + str(res))

def unique_tuple_frequency(test_list):
  
    freq_dict = {}
    for tup in test_list:
        sorted_tup = tuple(sorted(tup))
        if sorted_tup in freq_dict:
            freq_dict[sorted_tup] += 1
        else:
            freq_dict[sorted_tup] = 1
    return len(freq_dict)

# Initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# Printing original list
print("The original list is :" + str(test_list))

# Using dictionary and loop
res = unique_tuple_frequency(test_list)

# Printing result
print("Unique tuples Frequency : " + str(res))
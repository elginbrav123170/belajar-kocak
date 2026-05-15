# Python3 code to demonstrate working of
# Sort lists in tuple
# Using tuple() + sorted() + generator expression

# Initializing tuple
test_tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

# printing original tuple
print(&quot;The original tuple is : &quot; + str(test_tup))

# Sort lists in tuple
# Using tuple() + sorted() + generator expression
res = tuple((sorted(sub) for sub in test_tup))

# printing result
print(&quot;The tuple after sorting lists : &quot; + str(res))

# Python3 code to demonstrate working of
# Sort lists in tuple
# Using map() + sorted()

# Initializing tuple
test_tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

# printing original tuple
print(&quot;The original tuple is : &quot; + str(test_tup))

# Sort lists in tuple
# Using map() + sorted()
res = tuple(map(sorted, test_tup))

# printing result
print(&quot;The tuple after sorting lists : &quot; + str(res))

original_tuple = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

sorted_lists = ()
for lst in original_tuple:
    sorted_list = sorted(lst)
    sorted_lists += (sorted_list,)

print(sorted_lists)

tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

result_tup = tuple(map(lambda lst: sorted(lst), tup))

print(result_tup)
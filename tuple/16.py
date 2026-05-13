# Python3 code to demonstrate working of 
# Skew Nested Tuple Summation
# Using infinite loop

# initializing tuple
test_tup = (5, (6, (1, (9, (10, None)))))

# printing original tuple
print("The original tuple is : " + str(test_tup))

res = 0
while test_tup:
    res += test_tup[0]
    
    # assigning inner tuple as original
    test_tup = test_tup[1]

# printing result 
print("Summation of 1st positions : " + str(res))

# Python3 code to demonstrate working of 
# Skew Nested Tuple Summation
# Using recursion

# helper function to perform task
def tup_sum(test_tup):
    
    # return on None 
    if not test_tup:
        return 0
    else:
        return test_tup[0] + tup_sum(test_tup[1])

# initializing tuple
test_tup = (5, (6, (1, (9, (10, None)))))

# printing original tuple
print("The original tuple is : " + str(test_tup))

# calling fnc.
res = tup_sum(test_tup)

# printing result 
print("Summation of 1st positions : " + str(res))

def tup_sum(test_tup):
    # Base case: return 0 for empty tuple or tuple with no integer elements
    if not test_tup or not isinstance(test_tup[0], int):
        return 0
    else:
        # Recursively compute sum of first element of current tuple and remaining tuples
        return test_tup[0] + tup_sum(test_tup[1:])

# Example tuple
test_tup = (5, (6, (1, (9, (10, None)))))

# Print original tuple
print("The original tuple is:", test_tup)

# Compute sum of first elements
res = tup_sum(test_tup)

# Print result 
print("Sum of first elements:", res)

# Python3 code to demonstrate working of 
# Skew Nested Tuple Summation
# Using stack

# initializing tuple
test_tup = (5, (6, (1, (9, (10, None)))))


# function to compute sum of first elements using stack
def sum_first_elements(test_tup):
    stack = []
    res = 0
    stack.append(test_tup)

    while stack:
        curr = stack.pop()
        if isinstance(curr, int):
            res += curr
        elif curr:
            stack.append(curr[1])
            stack.append(curr[0])

    return res


# printing original tuple
print("The original tuple is : " + str(test_tup))

# printing result
print("Summation of 1st positions : " + str(sum_first_elements(test_tup)))

# Python3 code to demonstrate working of 
# Skew Nested Tuple Summation
# Using a generator function and sum

# define generator function to yield first element of each nested tuple
def get_first_element(tup):
    if isinstance(tup, tuple):
        yield tup[0]
        yield from get_first_element(tup[1])

# initializing tuple
test_tup = (5, (6, (1, (9, (10, None)))))


# printing original tuple
print("The original tuple is : " + str(test_tup))

# calculate sum of first elements using generator and sum
res = sum(get_first_element(test_tup))

# printing result 
print("Summation of 1st positions : " + str(res))
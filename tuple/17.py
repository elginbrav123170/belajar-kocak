# Python3 code to demonstrate working of 
# Convert Binary tuple to Integer
# Using join() + list comprehension + int()

# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# using int() with base to get actual number
res = int("".join(str(ele) for ele in test_tup), 2) 

# printing result 
print("Decimal number is : " + str(res))

# Python3 code to demonstrate working of
# Convert Binary tuple to Integer
# Using bit shift and | operator

# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))


res = 0
for ele in test_tup:

    # left bit shift and or operator
    # for intermediate addition
    res = (res << 1) | ele

# printing result
print("Decimal number is : " + str(res))

# Python3 code to demonstrate working of
# Convert Binary tuple to Integer

# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# using int() with base to get actual number
x = list(map(str, test_tup))
x = "".join(x)
res = int(x, 2)

# printing result
print("Decimal number is : " + str(res))

# Python3 code to demonstrate working of
# Convert Binary tuple to Integer

# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

res = 0
j = 0

for i in range(len(test_tup), 0, -1):
    x = 2**j
    res += x*test_tup[i-1]
    if(j > len(test_tup)):

        break

    j += 1

# printing result
print("Decimal number is : " + str(res))

binary_tuple = (1, 1, 0)
result = 0
length = len(binary_tuple)
for i in range(length):
    element = binary_tuple[length - i - 1]
    result = result + element*pow(2, i)
print("The output integer is:", result)

# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# using bit shifting and bitwise operations to get actual number
res = 0
for bit in test_tup:
    res = (res << 1) | bit

# printing result
print("Decimal number is : " + str(res))

def binary_tuple_to_int(binary_tup):
    if len(binary_tup) == 0:
        return 0
    else:
        return binary_tup[0] * 2**(len(binary_tup)-1) + binary_tuple_to_int(binary_tup[1:])
# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# calling recursive method
res = binary_tuple_to_int(test_tup)

# printing result
print("Decimal number is : " + str(res))
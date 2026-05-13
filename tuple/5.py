# Python3 code to demonstrate working of
# Elements Frequency in Mixed Nested Tuple
# using recursion + loop

# Helper function
def flatten(test_tuple):

    for tup in test_tuple:
        if isinstance(tup, tuple):
            yield from flatten(tup)
        else:
            yield tup

# Initializing tuple
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple
# Using recursion + loop

# Empty tuple
res = {}

# Iterating over list
for ele in flatten(test_tuple):
    if ele not in res:
        res[ele] = 0
    res[ele] += 1

# Printing result
print("The elements frequency : " + str(res))

# Python3 code to demonstrate working of 
# Elements Frequency in Mixed Nested Tuple
# using recursion + Counter()
from collections import Counter

# Helper function
def flatten(test_tuple):
  
    for tup in test_tuple:
        if isinstance(tup, tuple):
            yield from flatten(tup)
        else:
            yield tup

# Initializing tuple
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple
# using recursion + Counter()
res = dict(Counter(flatten(test_tuple)))

# Printing result 
print("The elements frequency : " + str(res))

# Python3 code to demonstrate working of
# Elements Frequency in Mixed Nested Tuple

# Initializing tuple
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple
x=[]
for i in test_tuple:
    if(type(i) is tuple):
        x.extend(list(i))
    else:
        x.append(i)
res=dict()
a=list(set(x))
for i in a:
    res[i]=x.count(i)
    
# Printing result
print("The elements frequency : " + str(res))

# Python3 code to demonstrate working of
# Elements Frequency in Mixed Nested Tuple
import operator as op
# Initializing tuple
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple
x=[]
for i in test_tuple:
    if(type(i) is tuple):
        x.extend(list(i))
    else:
        x.append(i)
res=dict()
a=list(set(x))
for i in a:
    res[i]=op.countOf(x,i)
    
# Printing result
print("The elements frequency : " + str(res))

from collections import defaultdict

def count_elements(t):
    freq = defaultdict(int)
    for item in t:
        if isinstance(item, int):
            freq[item] += 1
        elif isinstance(item, tuple):
            sub_freq = count_elements(item)
            for k, v in sub_freq.items():
                freq[k] += v
    return freq

# Example usage
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)
# Printing original tuple
print("The original tuple : " + str(test_tuple))
result = count_elements(test_tuple)
print("The elements frequency : " + str(result))
#This code is contributed by Vinay Pinjala.

def count_elements(t):

    # Empty dictionary
    freq = {}

    for item in t:
      
        if isinstance(item, int):
            if item not in freq:
                freq[item] = 0
            freq[item] += 1
        elif isinstance(item, tuple):
            for subitem in item:
                if isinstance(subitem, int):
                    if subitem not in freq:
                        freq[subitem] = 0
                    freq[subitem] += 1
    return freq


# Initializing list
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

result = count_elements(test_tuple)

# Printing answer
print("The elements frequency : " + str(result))

# This code is contributed by tvsk

# Python3 code to demonstrate working of
# Elements Frequency in Mixed Nested Tuple

# Initializing tuple
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple
x = str(test_tuple)

x = x.replace("(", "")
x = x.replace(")", "")
x = x.replace(",", "")

y = x.split()

y = list(map(int, y))
z = list(set(y))
res = dict()

for i in z:
    res[i] = y.count(i)

# Printing result
print("The elements frequency : " + str(res))
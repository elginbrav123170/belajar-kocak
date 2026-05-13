# Python3 code to demonstrate working of
# Extract K digit Elements Tuples
# Using all() + list comprehension

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# using len() and str() to check length and 
# perform string conversion
res = [sub for sub in test_list if all(len(str(ele)) == K for ele in sub)]

# printing result
print("The Extracted tuples : " + str(res))


# Python3 code to demonstrate working of
# Extract K digit Elements Tuples
# Using all() + filter() + lambda

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# filter() and lambda used for task of filtering
res = list(filter(lambda sub: all(len(str(ele)) == K for ele in sub), test_list))

# printing result
print("The Extracted tuples : " + str(res))

# Python3 code to demonstrate working of
# Extract K digit Elements Tuples

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initialising K
K = 2

res=[]
for i in test_list:
    x=list(map(str,i))
    p=[]
    for j in x:
        p.append(len(j))
    if(p==[K,K] or p==[K]):
        res.append(i)
    
# printing result
print("The Extracted tuples : " + str(res))


# Python3 code to demonstrate working of 
# Extract K digit Elements Tuples
# Using for loop and string slicing

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# using a for loop and string slicing to check length
res = []
for tup in test_list:
    flag = True
    for ele in tup:
        if len(str(ele)) != K:
            flag = False
            break
    if flag:
        res.append(tup)

# printing result
print("The Extracted tuples : " + str(res))
#This code is contributed by Vinay Pinjala.


# Python3 code to demonstrate working of
# Extract K digit Elements Tuples

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initialising K
K = 2

# Using a generator expression and tuple unpacking
res = tuple(t for t in test_list if all(len(str(e)) == K for e in t))

# printing result
print("The Extracted tuples : " + str(res))
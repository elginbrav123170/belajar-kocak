import heapq

tup = (5, 20, 3, 7, 6, 8)
K = 2

s = heapq.nsmallest(K, tup)
l = heapq.nlargest(K, tup)

print(s)
print(l)    

tup = (5, 20, 3, 7, 6, 8)
K = 2

temp = sorted(tup)
mi = temp[:K]
ma = temp[-K:]

print(mi)
print(ma)

tup = (5, 20, 3, 7, 6, 8)
K = 2

l = sorted(tup)
mi, ma = [], []

for i, val in enumerate(l):
    if i < K:
        mi.append(val)
    if i >= len(l) - K:
        ma.append(val)

print(mi)
print(ma)

tup = (5, 20, 3, 7, 6, 8)
K = 2

m1, m2 = [], []
for elem in tup:
    if len(m1) < K:
        m1.append(elem)
    else:
        if elem < max(m1):
            m1.remove(max(m1))
            m1.append(elem)

    if len(m2) < K:
        m2.append(elem)
    else:
        if elem > min(m2):
            m2.remove(min(m2))
            m2.append(elem)

m1.sort()
m2.sort(reverse=True)

print( m1)
print( m2)

tup = (5, 20, 3, 7, 6, 8)
K = 2

m1 = []
m2 = []
for ele in tup:
 
    if len(m1) < K:
        m1.append(ele)
    else:
        if ele < max(m1):
            m1.remove(max(m1))
            m1.append(ele)
    
    if len(m2) < K:
        m2.append(ele)
    else:
        if ele > min(m2):
            m2.remove(min(m2))
            m2.append(ele)

m1.sort()          
m2.sort(reverse=True) 

print(m1)
print( m2)

tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
K = 2

tl = list(tup)
m1 = []
m2 = []

i = 0
while i < K:
    val = min(tl)
    m1.append(val)
    tl.remove(val)
    i += 1

i = 0
while i < K:
    val = max(tl)
    m2.append(val)
    tl.remove(val)
    i += 1

m1.sort()
m2.sort(reverse=True)

print(m1)
print(m2)
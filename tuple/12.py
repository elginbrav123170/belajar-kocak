t = [(3, 4, 9), (5, 6, 7)]
tup = (1, 2, 5)
K =3
res = min(t, key=lambda x: abs(x[K-1] - tup[K-1]))
print(res)

t = [(3, 4, 9), (5, 6, 7)]
tup = (1, 2, 5)
K = 3

min_diff, res = float('inf'), None
for idx, val in enumerate(t):
    diff = abs(val[K-1] - tup[K-1])
    if diff < min_diff:
        min_diff, res = diff, idx

print(t[res])

import heapq

t = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
K = 2
res = heapq.nsmallest(1, t, key=lambda x: abs(x[K-1] - tup[K-1]))[0]
print(res)

t = [(3, 4, 9), (5, 6, 7)]
tup = (1, 2, 5)
K = 3
s = sorted(t, key=lambda x: abs(x[K-1] - tup[K-1]))
res = s[0]
print(res)
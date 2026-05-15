from collections import defaultdict

t = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
mapp = defaultdict(list)

for k, v in t:
    mapp[k].append(v)

res = [(k, *v) for k, v in mapp.items()]
print(res)

from itertools import groupby

t = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
res = []

for k, g in groupby(t, key=lambda x: x[0]):
    vals = [v for _, v in g]
    res.append((k, *vals))

print(res)

t = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
temp = {}

for x in t:
    temp[x[0]] = temp.get(x[0], []) + list(x[1:])

res = [(k,) + tuple(v) for k, v in temp.items()]
print(res)

def join_tup(t, i):
    if i == len(t) - 1:
        return t
    elif t[i][0] == t[i + 1][0]:
        t[i] += t[i + 1][1:]
        t.pop(i + 1)
        return join_tup(t, i)
    else:
        return join_tup(t, i + 1)

t = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
res = join_tup(t, 0)
print(res)
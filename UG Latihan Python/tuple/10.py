t = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
l = ['Geeks', 'best', 'CS', 'Gfg']

temp = dict(t)
res = [(key, temp[key]) for key in l]
print( res)

t = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
l = ['Geeks', 'best', 'CS', 'Gfg']

temp = {}
for key, ele in enumerate(l):
    temp.setdefault(ele, []).append(key)

res = sorted(t, key=lambda ele: temp[ele[0]].pop())
print( res)

from functools import reduce

t = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
l = ['Geeks', 'best', 'CS', 'Gfg']

res = reduce(lambda acc, key: acc + [ele for ele in t if ele[0] == key], l, [])
print( res)

t = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
l = ['Geeks', 'best', 'CS', 'Gfg']

res = sorted(t, key=lambda x: l.index(x[0]))
print(res)

from operator import itemgetter

l1 = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
l2 = sorted(l1, key=itemgetter(1))
print(l2)
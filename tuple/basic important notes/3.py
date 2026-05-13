a = [1, 2, 3, 4, 5]
res = [(n, n**3) for n in a]
print(res)

a = [1, 2, 3, 4, 5]
res = list(map(lambda n: (n, n**3), a))
print(res)

a = [1, 2, 3, 4, 5]
res = list(zip(a, [n**3 for n in a]))
print(res)

a = [1, 2, 3, 4, 5]
res = []
for n in a:
    res.append((n, n**3))
print(res)
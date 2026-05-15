import sys
tup = (0, 1, 2, 'a', 3)
print(sys.getsizeof(tup))

tup = (0, 1, 2,'a', 3)
res = memoryview(bytearray(str(tup),'utf-8'))
print(res.nbytes)

tup = (0, 1, 2, 'a', 3)
for item in tup:
    print(f"Memory address of {item}: {id(item)}")
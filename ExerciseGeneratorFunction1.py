def cyclic(iterable, n):
    for _ in range(n):
        for e in iterable:
            yield e
            
for i in cyclic("abc", 5):
    print(i, end=" ")
print()
d=list(cyclic([1,2,3,4,5], 3))
print(d)
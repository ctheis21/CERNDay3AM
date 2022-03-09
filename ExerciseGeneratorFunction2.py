import time
import operator
import functools


def factorial(nb):
    if nb <= 0:
        return None
    elif nb ==0 :
        return 1
    else:
        return functools.reduce(operator.mul, range(1,nb+1))

def elapsed_time(data):
    last_time = None
    for item in data:
        result=factorial(item)
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item, result)
        
        
        
numbers=(2,3,4,5,6,7,8,20,30,200)

for t in elapsed_time(numbers):
    print(t)

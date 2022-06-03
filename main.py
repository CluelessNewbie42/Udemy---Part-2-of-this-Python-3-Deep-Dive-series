# Reverse items from a list

'''l1 = [1, 2, 4, 6, 6, 9, 9]
l2 = []

while l1 != []:
    for i in l1:
        if i == l1[-1]:
          l2.append(i)
          l1.remove(i)
print(l2)
'''
#This code shows a graph of the time complexity of the reverse() function.
import copy

'''import matplotlib.pyplot as plt
import time

y = []
for i in [100000 * j for j in range(10,100)]:
    lst = list(range(i))
    t0 = time.time()
    x = lst.reverse()
    t1 = time.time()
    y.append(t1-t0)


plt.plot(y)
plt.xlabel("List elements (10**5)")
plt.ylabel("Time (sec)")
plt.show()'''

'''list_1 = [1, 2, 3, 4, 5, 6]

y = map(lambda i: i**2, list_1)

print(list(y))'''

'''def generator(n):
    for i in range(n):
        yield i

for i in generator(5):
    print(i)'''

#Cool Python syntax
'''a = 4
b = 3
x = 0 if a > b else 1
print(x)
a = 3
b = 4
x = 0 if a > b else 1
print(x)'''

'''import copy
var1 = (2, 1)

var1copy = copy.copy(var1)

print(var1copy)
print(id(var1), id(var1copy))

var1_deep_copy = copy.deepcopy(var1)

print(var1_deep_copy)
print(id(var1), id(var1_deep_copy))'''

#slicing always return a new object. The id will be different.


#SLICING
#this first example is cool!

'''l = [1, 2, 3, 4, 5, 6, 7]
s = slice(0, 2)

print(l[s])'''

#
'''
from functools import lru_cache

@lru_cache(2 * 10)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)

    @staticmethod
    @lru_cache(2*10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)

f = Fib(100)

print(list(f))'''


#In-place concatenation +=
#When using += to concatenate objects, the location of the new object remains the same as the first object.
#Example:
'''l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(id(l1))
print(id(l2))

l1 += l2

print(id(l1))

# However, for regular concatenation, the location of the object will change:

l1 = l1 + l2

print(id(l1))'''



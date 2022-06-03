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

l = [1, 2, 3, 4, 5, 6, 7]
s = slice(0, 2)

print(l[s])
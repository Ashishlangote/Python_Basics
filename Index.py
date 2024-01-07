# import matplotlib.pyplot as plt
# import numpy as np

# class A:
#     def fun(self):
#         print("Public")

#     def __fun(self):
#         print("Private")
#
#
# obj = A()
# obj._A__fun()


d1 = {'a': "b", 'b': "c"}
d2 = {'c': "d", 'd': "k"}

x = {**d1, **d2}
print(x)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

c = [*l1, *l2]
print(l1 + l2)

y = [x for x in l1]
print(y)

s1 = {1, 2, 3}
s2 = {4, 5, 6}

print({*s1, *s2})

l = [1, 2, 3, 4, 5, 6]
l1 = []
for i in l:
    for j in l:
        if i + j == 7:
            l1.append((i, j))
print(l1)

from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


print([c for c in Color])

t = tuple('lupins')
print(list(t))

t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2
print(t3)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
a = zip(l1, l2)
print(list(a))

test_keys = ["Rash", "Kil", "Harsh"]
test_values = [1, 4, 5]
res = dict(zip(test_keys, test_values))
print(str(res))
print(str(res))

for i in range(4):
    if i == 2:
        break
    print(i)

for i in range(5):
    print(i, end=" ")
    if i == 3:
        break
    print("Hello")

e = []
o = []

l = [1, 2, 4, 5, 6, 7, 8, 9, 10]


def even(a):
    for i in a:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    return e, o


even(l)
print("Even: ", e)
print("Odd: ", o)

t1 = (1, 2, 3, 4)
t2 = (4, 5, 6, 5)
t3 = []

for i in range(0, len(t1)):
    t3.append(t1[i] + t2[i])

print(tuple(t3))

# i = input('Enter: ')
# l = i.split(',')
# t = tuple(l)
# print(l)
# print(t)

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = []

# for i in range(0, len(x)):
#     z.append((x[i], y[i]))

# print(z)

# numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# sum_ = sum(numbers)
# print(sum_)

# sum_ = sum(numbers, 20)
# print(sum_)

# a = ["1", "2", "-3"]
# print(list(map(int, a)))

# c = 12345

# d = [int(i) for i in str(c)]

# for i in d:
#     print(i)


# D = dict()

# for x in enumerate(range(2)):
#     D[1] = x[1]
#     D[2 + 2] = x[0]

# print(D.values())
# print(D)

# x = [i for i in range(2)]
# y = enumerate(x)

# print(dict(y))


# def gen():
#     yield 1
#     yield 2


# iterable = gen()
# for a in iterable:
#     print(a)
# # What was the first item of iterable? No way to get it now.
# # Only to get a new iterator
# gen()


# Write a program to find frequency of each word in a paragraph

"""
Input: This is python class. Python is interactive language.

Output:
this: 1
is: 2
python: 2
interactive: 1
class: 1
language: 1
"""


# var = "This is python class. Python is interactive language."

# var = var.lower()
# var = var.replace('.', ' ')
# word_list = var.split()
# unique_word =set(word_list)

# for word in unique_word:
#     print(word,":",word_list.count(word))


class MyBaseClass:
    def __init__(self, base_attr):
        self.base_attr = base_attr


class MyDerivedClass(MyBaseClass):
    def __init__(self, base_attr, derived_attr):
        # Accessing base class attribute directly
        MyBaseClass.base_attr = base_attr
        self.derived_attr = derived_attr

    def print_attrs(self):
        print("Base attribute:", self.base_attr)
        print("Derived attribute:", self.derived_attr)


obj = MyDerivedClass("base value", "derived value")
obj.print_attrs()

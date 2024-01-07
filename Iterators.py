# In Python, an object which implements the __iter__() method is called on iterable.

# Iterator in Python is simply an object that can return data one at a time while iterating over it.

# The __next__() method returns the next value in the iteration and updates the state to the next value.

numbers = [1, 2, 3]

value = iter(numbers)

print(next(value))
print(next(value))
print(next(value))
# print(next(value)) will raise StopIteration error

print("---------------------")

# Trying with infinite while loop
numbersList = [1, 2, 3]

iterObj = iter(numbersList)


while True:
    try:
        element = next(iterObj)
        print(element)
    except StopIteration:
        break

print("---------------------")

class Even:

    def __init__(self, max):

        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):

        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


numbers = Even(10)

for i in numbers:
    print(i)


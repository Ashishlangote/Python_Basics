'''
Python decorator is a function that takes in another function adds some functionality to it and then return's it.
'''


def inc(x):
    return x + 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))

print("----------------")


# In Python, we can also define a function inside a function.


def print_msg(message):

    greeting = "Hello"

    def printer():
        print(greeting, message)
    printer()


print_msg("Python")

print("----------------")

# Function can also return another function as a value


def print_msg(message):

    greeting = "Hello"

    def printer():
        print(greeting, message)

    return printer


func = print_msg("Python")
func()

print("----------------")

'''
A Python decorator is function that takes in a function, adds some functionality to it and returns the original function.
'''


def printer():
    print("Hello")


def display_info(func):

    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")

    return inner


decorator = display_info(printer)
decorator()


print("----------------")

# With @ symbol


def display_info(func):

    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")

    return inner


@display_info
def printer():
    print("Hello")


printer()

print("----------------")

# Decorating Functions with Parameters


def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
        if b == 0:
            print("Cannot divided by 0")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a / b


a = divide(50, 0)
print(a)

print("----------------")

# Chaining Decorators in Python


def star(func):

    def inner(arg):
        print("*" * 10)
        func(arg)
        print("*" * 10)
    return inner


def percent(func):

    def inner(arg):
        print("%" * 10)
        func(arg)
        print("%" * 10)

    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
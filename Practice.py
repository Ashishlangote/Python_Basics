num = 11
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# Fibonacci sequence:

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < nterms:
    print(n1)
    n1, n2 = n2, n1 + n2
    count += 1

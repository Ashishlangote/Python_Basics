# Returns True if n is a perfect square, and False otherwise

def is_perfect_square(n):
    return (n ** 0.5).is_integer()


numbers = [3, 4, 37, 9, 7, 32, 25, 81, 79, 100]

perfect_squares = filter(is_perfect_square, numbers)

print(list(perfect_squares))

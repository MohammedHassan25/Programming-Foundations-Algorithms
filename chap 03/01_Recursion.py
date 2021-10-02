# --------------------------------------------------------------------
# Recursion is when a function calls itself
# Recursion functions need to have a breaking condition
# This prevents infinite loops and eventual crashes
# Each time the function is called, the old arguments are saved
# This is called the "call stack"
# --------------------------------------------------------------------

# Simple recursion example

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, '....')
        countdown(x-1)
        print('moh')


countdown(8)

# Power and factorial


def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


print(power(5, 3))   # is equal to 5^3 (5 ** 3)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))    # is equal to 5x4x3x2x1

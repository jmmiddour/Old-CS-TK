import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


lookup_table = {}  # Cache, which is kind of like a dictionary


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # key = (x, y)
    #
    # if key in lookup_table:
    #     return lookup_table[key]
    #
    # v = math.pow(x, y)
    # v = math.factorial(v)
    # v //= (x + y)
    # v %= 982451653
    # lookup_table[key] = v
    # return lookup_table[key]

    if (x, y) not in lookup_table:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        lookup_table[(x, y)] = v
    return lookup_table[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

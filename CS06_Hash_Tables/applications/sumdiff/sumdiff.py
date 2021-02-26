"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

cache = {}


def f(x):
    if x not in cache:
        cache[x] = x * 4 + 6

    return cache[x]


for a in q:
    for b in q:
        res = f(a) + f(b)
        for c in q:
            for d in q:
                if res == f(c) - f(d):
                    print(a, b, c, d)


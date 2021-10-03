# -----------------------------------------------------------------------------------------------------
# So unfortunately, searching an unordered list can be pretty inefficient so lets go back to the code
# -----------------------------------------------------------------------------------------------------

m = [6, 7, 5, 33, 88, 47, 25, 36, 48]


def f(e, n):
    for i in range(0, len(m)):
        if e == n[i]:
            return i

    return None


print(f(88, m))
print(f(200, m))

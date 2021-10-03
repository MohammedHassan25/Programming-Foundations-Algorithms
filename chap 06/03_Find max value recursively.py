m = [2, 8, 5, 6, 88, 20, 35, 56]


def findmax(m):
    if len(m) == 1:
        return m[0]

    op1 = m[0]
    print(op1)
    op2 = findmax(m[1:])
    print(op2)

    if op1 > op2:
        return op1
    else:
        return op2


print("The largest number is", findmax(m))

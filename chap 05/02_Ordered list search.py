# -----------------------------------------------------------------------------------------------------
# Searching for data in an ordered, or sorted list, is much more efficient than for an unordered list.
# -----------------------------------------------------------------------------------------------------

m = [6, 8, 19, 20, 23, 41 ,48, 50, 66, 71]

def f(e,n):
    ls = len(n) - 1
    Low = 0
    Upp = ls
    while Low <= Upp:
        mid = (Low + Upp)//2
        if n[mid] == e:
            return mid
        elif e > n[mid]:
            Low = mid + 1
        else:
            Upp = mid -1

    if Low > Upp:
        return None

print(f(20,m))
print(f(48,m))
print(f(100,m))
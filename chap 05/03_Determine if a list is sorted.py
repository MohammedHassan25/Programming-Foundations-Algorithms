# ------------------------------------------------------------------------------------------------------------------------------
# As more items get added to the input list, the number of operations needed to check each item increases correspondingly.
# ------------------------------------------------------------------------------------------------------------------------------

m1 = [6, 8, 19, 20, 23, 41, 48, 50, 66, 71]
m2 = [8, 19, 6, 41, 20, 23, 48, 66, 71, 50] 

def issorted(list):
    for i in range(0, len(list)-1):
        if (list[i] > list[i+1]):
            return False
    return True

print(issorted(m1))
print(issorted(m2))
# ----------------------------------------------------------------------------------------
# Search algorithms : find specific data in a structure
# Sorting algorithms : Take a dataset and apply a sort order to it
# Computational algorithms : Given one set of data, calcuate another
# Collection algorithms : Work with collections of data
# ----------------------------------------------------------------------------------------

# ex :
def gcd(a, b):
    while (b != 0):
        t = a     # t = 20 and then t = 7 and then t = 6
        a = b     # a = 7 and then a = 6 and then a = 1
        b = t % b     # new b = 20 % 7 and then new b = 7 % 6 and then new b = 6 % 1 = 0 and stop loop operation

    return a


print(gcd(20, 7))

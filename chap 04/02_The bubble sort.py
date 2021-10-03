# --------------------------------------------------------------
# Characteristics the bubble sort :-
# Very simple to understand and implement
# Performance: O(n^2)    # Time complexity of the second order
# Other sorting algorithms are generaly much better
# Not considered to be a practical solution
# --------------------------------------------------------------

# for example

def bubbleSort(dataset):
    for a in range(len(dataset) -1,0,-1):
        for m in range(a):
            if dataset[m] > dataset[m+1]:
                t = dataset[m]
                dataset[m] = dataset[m+1]
                dataset[m+1] = t
    print("Current state: ", dataset)

def main():
    list1 = [6, 7, 5, 44, 66, 22, 33, 11, 25]
    bubbleSort(list1)
    print('Result: ', list1)

if __name__ == '__main__':
    main()
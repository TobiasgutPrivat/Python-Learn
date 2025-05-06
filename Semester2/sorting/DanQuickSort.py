import random

def quicksort(values, start=0, end=None):
    if end is None:
        end = len(values) - 1
    # print(start, end)
    if start < end:
        pivot = partition(values, start, end)
        quicksort(values, start, pivot-1)
        quicksort(values, pivot+1, end)
    return values

def partition(values, start, end):
    #choose a random index
    r = random.randint(start, end)
    #retrieve the pivot element at this index
    pivot = values[r]
    #now exchange the pivot element with the last element
    #from the list. This makes sure that we know where the
    #element is and can put it in the middle between both
    #lists.
    exchange(values, r, end)
    #^cont

    #iterate from start to end over our list. Note that
    #i will be incremented before first use.
    i = start - 1

    for j in range(start, end):
        #if we find an element smaller than our pivot,
        #exchange it with the value at position i+1, where
        #the first element larger than our pivot is stored.
        if values[j] <= pivot:
            i += 1
            exchange(values, i, j)
    #finally, exchange our pivot back from the last element
    exchange(values, i+1, end)
    #and return the pivot index
    return i+1

def exchange(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
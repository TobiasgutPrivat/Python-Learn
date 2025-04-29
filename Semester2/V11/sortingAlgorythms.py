def swapSort(lst: list):
    for i in range(len(lst) - 1):
        j = i
        while j >= 0 and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1
    return lst

def insertSort(lst: list):
    # strategy: for each element, find the right place in the sorted part of the list and insert it there
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def insertBinarySort(lst: list):
    # strategy: for each element, find the right place in the sorted part of the list and insert it there, but use binary search to find the right place
    for i in range(1, len(lst)):
        key = lst[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            if key < lst[mid]:
                high = mid - 1
            else:
                low = mid + 1
        lst[low + 1:i + 1] = lst[low:i] # move all entries to the right (a lot faster than moving all entries one by one)
        # for j in range(i - 1, high, -1):
        #     lst[j + 1] = lst[j]
        lst[low] = key
    return lst

def quickSort(lst: list):
    # strategy: choose a pivot, partition the list into two parts (less than pivot and greater than pivot), and sort each part recursively
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    right = [x for x in lst if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

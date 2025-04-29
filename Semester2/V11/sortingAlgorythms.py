def swapSort(lst: list):
    for i in range(len(lst) - 1):
        j = i
        while j >= 0 and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1

def insertSort(lst: list):
    # strategy: for each element, find the right place in the sorted part of the list and insert it there
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

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
        for j in range(i - 1, high, -1):
            lst[j + 1] = lst[j]
        lst[low] = key

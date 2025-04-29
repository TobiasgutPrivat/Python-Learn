import random
import time
from sortingAlgorythms import *

def BenchmarkSorting(sortFunc: callable) -> int: # returns average time in seconds
    iterations = 1
    total_time = 0
    for _ in range(iterations):
        list = [random.random() for _ in range(0,10000)]
        start_time = time.time()
        sortedList = sortFunc(list)
        total_time += time.time() - start_time
        if sortedList != sorted(list):
            raise ValueError("sorting didn't work correctly",sortedList,sorted(list))
    return total_time / iterations
    
if __name__ == "__main__":
    print("swapSort        ",BenchmarkSorting(swapSort))
    print("insertSort      ",BenchmarkSorting(insertSort))
    print("insertBinarySort",BenchmarkSorting(insertBinarySort))
    print("quickSort       ",BenchmarkSorting(quickSort))
    print("builtInSort     ",BenchmarkSorting(sorted))
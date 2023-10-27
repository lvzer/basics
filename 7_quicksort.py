# partition(), divide and conquer, efficient on large data sets, not good for small datasets
# average case theta(n logn), very good in practice, one of the fastest sorting algos
# worst case O(N2)

import random

def partition(list, low, high):
    # choosing the last element as pivot
    pivot = list[high]
    #pointer for greater element
    i = low - 1
    for j in range(low, high):
        # element smaller than pivot: swap it with greater element pointed by i
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    # swap pivot with greater element
    list[i+1], list[high] = list[high], list[i+1]

    # return index @ which partition is done
    return i+1


def quicksort(list, low, high):
    if low < high:
        # < pivot = left, > pivot = right
        pivot = partition(list, low, high)
        quicksort(list, low, pivot-1)
        quicksort(list, pivot+1, high)

randomlist = random.sample(range(0, 100), 5)
print("The list is: ", randomlist)
n = len(randomlist)
quicksort(randomlist, 0, n-1)
print("The sorted list is: ", randomlist)
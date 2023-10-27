# keep diving into halves and mergesort recursively
# O(nlogn), not optimal for small datasets, good for large datasets

import random

def mergesort(list):
    if len(list) > 1:
        middle = len(list)//2
        left = list[:middle]
        right = list[middle:]
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i = i+1
            else:
                list[k] = right[j]
                j = j+1
            k += 1

        # In case anything is left in the remaining lists:
        while i<len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            list[k] = right[j]
            j += 1
            k += 1


randomlist = random.sample(range(0, 100), 5)
print("The list is: ", randomlist)
mergesort(randomlist)
print("The sorted list is: ", randomlist)
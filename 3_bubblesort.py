# Compare two elements, if 1 > 2, swap them and repeat iterations
# Time Complexity: O(N^2), very slow for large datasets
import random 

def bubblesort(rlist):
    n = len(rlist)
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if rlist[j] > rlist[j+1]:
                rlist[j], rlist[j+1] = rlist[j+1], rlist[j]
                swapped = True
        
        # If the element isn't bigger, then move to the next
        if swapped == False:
            break


randomlist = random.sample(range(0, 100), 10)
print("The list is: ", randomlist)
bubblesort(randomlist)
print("The sorted list is: ", randomlist)
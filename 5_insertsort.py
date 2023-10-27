# worst case: O(n^2)
import random 

def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j>=0 and key<list[j]:
            list[j+1] = list[j]
            j = j - 1
        
        list[j+1] = key


randomlist = random.sample(range(0, 100), 5)
print("The list is: ", randomlist)
insertionsort(randomlist)
print("The sorted list is: ", randomlist)
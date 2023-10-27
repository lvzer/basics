# move smallest to left, repeat
# Time Complexity: O(N^2), very slow for large datasets
import random 

def selectionsort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        
        list[i], list[min] = list[min], list[i]


list = random.sample(range(0, 100), 5)
print("The list is: ", list)
selectionsort(list)
print("The sorted list is: ", list)
# Binary Search on a sorted list
# O(logN)
# has to be sorted

# halves, check middle, split again
def binary_search(list, left, right, x):
    if right >= left:
        middle = left + (right-1) // 2
        if list[middle] == x:
            return middle
        
        elif list[middle] > x: # Go left
            return binary_search(list, left, middle-1, x)
        
        else:                 # Go right
            return binary_search(list, middle+1, right, x)
    else:
        return -1


list = [1, 12, 23, 34, 45, 61, 72, 81, 90, 110]
x = int(input("Enter the number you want to search for: "))
index = binary_search(list, 0, len(list)-1, x)
if index != -1:
    print("Found at index: ", index)
else:
    print("Not found")
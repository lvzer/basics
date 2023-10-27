# Linear Search to find an element in a list
# Linear search has a time complexity of O(N), slow for large datasets.

def linear_search(List, n):
    for i in range(len(List)):
        if(List[i] == n):
            return True
    return False

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Enter the number you want to search for: "))
if linear_search(list, x):
    print("Found")
else:
    print("Not found")
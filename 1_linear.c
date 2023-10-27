// Linear Search to find an element in a list

#include<stdio.h>

int linear_search(int arr[], int n, int x){
    for(int i = 0; i < n; i++){
        if(arr[i] == x)
            return i;
    }
    return 0;
}

void main(){
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int x;
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("Enter the number you want to search for: ");
    scanf("%d", &x);

    int result = linear_search(arr, n, x);
    if(result == 0){
        printf("Element not found");
    }else{
        printf("Element found at index %d", result);
    }
}
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        print(arr)
        
        for j in range(0, n - i - 1):
    
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr

arr1=[10,5,4,7,8,2,3,9]
bubble_sort(arr1)
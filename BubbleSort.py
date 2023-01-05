def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        print(arr)
        
        for j in range(0, n - i - 1):
    
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

ar=[10,5,4,7,8,2,3,9]
bubbleSort(ar)
def SelectionSort(arr):
    length = len(arr)
    
    for i in range(length):
        min = i
        print(arr)
        for j in range(i + 1, length):
            if arr[min] > arr[j]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            
    return arr

arr1=[6,3,2,1,4]
SelectionSort(arr1)
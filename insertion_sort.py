def insertion_sort(arr):
    length=len(arr)
    
    for i in range(length):
        print(arr)
        
        for j in range(i+1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        
    
    return arr

arr1=[5,9,2,4,7,1,10]
insertion_sort(arr1)

# 결과값
# [5, 9, 2, 4, 7, 1, 10]
# [1, 9, 5, 4, 7, 2, 10]
# [1, 2, 9, 5, 7, 4, 10]
# [1, 2, 4, 9, 7, 5, 10]
# [1, 2, 4, 5, 9, 7, 10]
# [1, 2, 4, 5, 7, 9, 10]
# [1, 2, 4, 5, 7, 9, 10]
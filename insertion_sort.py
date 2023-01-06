def insertion_sort(arr):
    length=len(arr)
    
    for i in range(length):
        print(arr)
        #외부 반복문의 i에 해당하는 원소와 다음 원소를 비교하기 위해
        #j의 범위를 아래와 같이 한다.
        
        for j in range(i+1, length):
            #외부 반복문에 i에 해당하는 원소와 j를 비교하고, i가 더
            #작다면 위치를 바꿔준다.
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
def selection_sort(arr):
    length = len(arr)
    
    for i in range(length):
        # 나중에 비교를 위해 i(인덱스값)을 다른 변수(min)에 저장해둔다
        min = i
        print(arr)
        # 해당하는 회전의 i에 해당하는 원소와 나머지를 비교하기 위해 아래와 같은 range를 설정해준다.
        for j in range(i + 1, length):
            # arr[min]과 arr[j]를 비교해서 전자가 더 작을경우 min에 j값을 넣어준다
            if arr[min] > arr[j]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            
    return arr

arr1=[6,3,2,1,4]
selection_sort(arr1)

# 결과값
# [6, 3, 2, 1, 4]
# [1, 3, 2, 6, 4]
# [1, 2, 3, 6, 4]
# [1, 2, 3, 6, 4]
# [1, 2, 3, 4, 6]
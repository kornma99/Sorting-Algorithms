def merge_sort(arr) :
    
    if len(arr) <= 1 :
        return arr
    
    #리스트를 반으로 쪼개기
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    #반으로 계속 쪼갠다. 더 이상 쪼개지지 않을 경우 위에 if문에 의해 arr을 return한다.
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    
    return merge(left_, right_)


def merge(left, right) :
    i, j = 0,0
    final_arr = []
    
    while i < len(left) and j < len(right):

        if left[i] < right[j] :
            final_arr.append(left[i])
            i += 1
            
        else:
            final_arr.append(right[j])
            j += 1
    while i < len(left):
        final_arr.append(left[i])
        i += 1
    while j < len(right):
        final_arr.append(right[j])
        j += 1
    return final_arr

arr1 = [8,10,7,9,2,4,3,1,18,17,14]
print(merge_sort(arr1))

# 결과값
# [1, 2, 3, 4, 7, 8, 9, 10, 14, 17, 18]
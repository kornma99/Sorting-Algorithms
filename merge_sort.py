def merge_sort(arr) :
    
    if len(arr) <= 1 :
        return arr
    
    middle = len(arr) // 2
    
    lowar = arr[ :middle]
    highar = arr[middle: ]
    
    lowar_ = merge_sort(lowar)
    highar_ = merge_sort(highar)
    
    return merge(lowar_, highar_)


def merge(list1, list2) :
    i,j = 0,0
    final_arr = []
    print(final_arr)
    
    while i < len(list1) and j < len(list2):

        if list1[i] < list2[i] :
            final_arr.append(list1[i])
            i += 1
            
        else:
            final_arr.append(list2[i])
            j += 1
        
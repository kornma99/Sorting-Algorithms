import random as rnd
import time
import numpy as np
 
 
sortedArr = []
arr = []
SIZE = 11
RANGE = 14234
 
 
# 정렬된 상태인지 체크
def isSorted():
    if(np.array_equal(arr, sortedArr)):
        return True
    else:
        return False
 
 
def shuffle() :
    global arr
    
    for i in range(SIZE):
        index1 = rnd.randrange(0, SIZE)
        index2 = rnd.randrange(0, SIZE)
        
        # 인덱스 교환(swap)
        arr[index1], arr[index2] = arr[index2], arr[index1]
        
 
def Bogosort():
    shuffle_count = 0
    global sortedArr
    global arr 
 
    for i in range(SIZE):
        val = rnd.randrange(0, RANGE)
        arr.append(val)
        sortedArr.append(val)
    
    # 사전 정렬 배열 정렬 
    sortedArr.sort()
    
    # 정렬되지 않은 배열 출력
    print("[Not Sorted array]")
    print(arr)
    
    # 정렬된 배열 출력
    print("[Sorted array]")
    print(sortedArr)
    
    # 타임 체크
    start = time.time()
    #정렬될 때 까지 계속 셔플한다
    while(isSorted() == False):
        shuffle()
        shuffle_count= shuffle_count + 1
    
    end = time.time()
    print("Shuffle count : ",end = '')
    print(shuffle_count)
    print("Time : ", end = '')
    print(end - start)
    
    sortedArr.clear()
    arr.clear()
        
        
for i in range(7):
    Bogosort()
    print()
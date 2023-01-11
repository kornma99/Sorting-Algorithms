# 힙 정렬 (복붙버전. 공부 필요)
def heapify(unsorted, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  
  if left < heap_size and unsorted[right] > unsorted[largest]:
    largest = left
    
  if right < heap_size and unsorted[right] > unsorted[largest]:
    largest = right
    
  if largest != index:
    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
    heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
  n = len(unsorted)
  
  for i in range(n // 2 - 1, -1, -1):
    heapify(unsorted, i, n)
    
  for i in range(n - 1, 0, -1):
    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
    heapify(unsorted, 0, i)

  return unsorted
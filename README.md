# **정렬 알고리즘**  </br></br>
</br>

###  정렬 알고리즘들의 시간복잡도별 정리
</br>

---

</br>

 - 알고리즘의 시간복잡도</br>

	* O(n²)의 시간 복잡도
		- [버블 정렬 (Bubble sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/BubbleSort.py)
    	- [선택 정렬 (Selection sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/InsertionSort.py)
		- [삽입 정렬 (Insertion sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/InsertionSort.py)
</br></br>  
    * O(nlogn)의 시간 복잡도
        - [합병 정렬/머지 정렬 (Merge sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/MergeSort.py)
        - [퀵 정렬 (Quick sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/QuickSort.py)
        - [힙 정렬 (heap sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/HeapSort.py)
</br></br> 
    * 그 외의 시간 복잡도를 가지는 정렬과 재밌는 정렬
        - [쉘 정렬 (Shell sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/ShellSort.py) [ O(n²) ~ O(nlogn) ]
        - [보고 정렬 (Bogo sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/BogoSort.py) [ O((n+1)!) ]
</br></br>

---

</br></br>


- ###  O(n²) 의 시간 복잡도를 가지는 알고리즘들
  
    n²의 시간 복잡도를 가지는 정렬 알고리즘들의 공통적인 장점은 구현이 쉽다는 것이다. 제어문의 기본만 알고 있어도 바로 구현 가능하다.

    그러나 효율이 상당히 좋지 않다. 하나하나 비교해가면서 정렬하기 때문에 **시간**이 오래 걸리는 큰 단점이 있다.

  1. [버블 정렬 (Bubble sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/BubbleSort.py)

        버블 정렬은 기본적으로 2개의 제어문을 이용해 리스트의 인접한 두 원소를 비교하여 왼쪽의 원소가 더 클 경우 둘의 자리를 바꾸는 방식을 반복한다.

        그렇다면 첫 회전에는 가장 큰 원소가 제일 뒤로 가게 되고, 다음 회전에는 두번째로 큰 숫자가 그 뒤에 가게 된다. 이것을 n-1번 반복하면 리스트는 정렬된다.

        첫 회전에는 n-1번, 두번째에는 n-2, 계속 반복하다가 마지막 회전에는 1번의 비교를 마칠 것이다.
        그렇다면 전체 비교 횟수는 n(n-1)/2가 될 것이다. 
        
        시간 복잡도는 O(n²)</br></br>

  2. 선택 정렬 (Selection sort)
        
        선택 정렬은 2개의 제어문을 이용해 첫번째 회전에는 가장 작은 원소를 앞으로, 두번째 제어문에서는 그 다음으로 작은 원소를 앞에서 두번째로 보내는 것을 반복하면서 정렬하는 방법이다.

        첫번째 제어문에서는 n-1번 반복하고, 두번째 내부 제어문에서는 최솟값을 찾기 위해 n-1,n-2,n-3,...,2,1번 반복한다.
        그렇다면 전체 비교 횟수는 역시 n(n-1)/2.

        시간 복잡도는 O(n²)</br></br>
  
  3. 삽입 정렬 (Insertion sort) 
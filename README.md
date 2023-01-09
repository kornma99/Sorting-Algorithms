# <center> **정렬 알고리즘** </center>  </br></br>
</br>

### <center>  정렬 알고리즘들의 시간복잡도별 정리 </center>
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
        - [힙 정렬 (Heap sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/HeapSort.py)
</br></br> 
    * 그 외의 시간 복잡도를 가지는 정렬과 재밌는 정렬
        - [쉘 정렬 (Shell sort)](https://github.com/kornma99/Sorting-Algorithms/blob/main/ShellSort.py) [ O(n²) ]
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

        까다로운 점은 다른 원소들의 인덱스 변화는 없이 해당하는 순서의 원소와 그 순서에 맞는 작은 원소의 위치를 바꿔줘야 하는 것이다. 이것을 위해 if문을 이용한다.

        첫번째 제어문에서는 n-1번 반복하고, 두번째 내부 제어문에서는 최솟값을 찾기 위해 n-1,n-2,n-3,...,2,1번 반복한다.
        그렇다면 전체 비교 횟수는 역시 n(n-1)/2.

        시간 복잡도는 O(n²)</br></br>
  
  3. 삽입 정렬 (Insertion sort)
        
        삽입 정렬은 선택 정렬과 방식이 비슷하다. 그러나 제어문을 통한 회전에서 해당하는 인덱스의 원소와 비교되는 원소가 작을 경우, 무조건 바꾼다. 이러한 방식으로 한바퀴 돌면 해당 원소와 가장 작은 원소의 위치만 바뀌는 선택정렬과는 달리 가장 작은 원소가 제일 앞으로 오기 하지만, 나머지 원소들의 위치도 뒤죽박죽이 되게 된다.

        이 정렬방법 또한 첫 회전때 n-1개의 비교를 하고, 두번째 자리에 들어올 두번째로 작은 원소를 찾기 위해 n-2개의 비교를 하게 된다. 반복하면 전체 횟수는n(n-1)/2가 된다.

        시간 복잡도는 O(n²)</br></br>
---
</br></br>
- ###  O(nlogn) 의 시간 복잡도를 가지는 알고리즘들

    분할 정복(Divide and conquer)방식을 사용하는 알고리즘들이다.
    nlog의 시간 복잡도를 가지는 알고리즘들은 기본적으로 데이터를 반으로 쪼갠다는 개념을 기본으로 가져간다. 둘씩 짝지어서 계속 반복하는 O(n²) 의 시간 복잡도를 가지는 알고리즘들과는 다르게 반복할수록 반복해야하는 횟수가 반으로 줄어들기 때문에 시간의 효율이 좋다. 
</br></br>

  1. 합병 정렬/머지 정렬 (Merge sort)

        합병 정렬은 주어진 배열을 첫 회전에는 2개로, 다음 회전에는 4개로, 반복하여 쪼개어 리스트에 하나의 원소만 있을 때까지(더이상 쪼갤 수 없을 때까지) 쪼갠다.
        이후 두개씩 합치기를 하는데, 이때 중요한 점은 합칠 때 작은 숫자가 앞으로 오게 위치시키는 것이다. 이러한 방식을 반복하면 정렬이 완료된다.

        이 정렬방법은 원소가 더이상 쪼개지지 않을 때까지 반으로 쪼개는 작업을 반복한다. 그럼 쪼개는 행위 자체의 시간복잡도는 O(logn)가 된다. 여기서 쪼개진 데이터 그룹의 개수만큼 다시 합치게 되니 n을 곱해준다.
        
        시간복잡도는 O(nlogn)이 된다. 
</br></br>


    2.  퀵 정렬 (Quick sort)
        
        퀵 정렬은 합병 정렬과 마찬가지로 분할 정복(Divide and Conquer)과 재귀 함수를 이용한 알고리즘이다.

        퀵 정렬은 처음 배워보는 피봇(pivot)이라는 임의의 기준값을 사용한다. 합병 정렬은 정 가운데를 기준으로 잡지만, 퀵 정렬은 이 피봇을 이용해서 나눈다.
        피봇을 기준으로 나누면 2개로 분할된다. 이 두 배열 사이는 피봇을 기준으로 나뉘였으니 높고 낮은것이 확실하다.

        이제 왼편을 새로운 임의의 기준값을 이용해 나누고, 오른쪽도 동일하게 나눠준다. 이것을 반복하다 보면 하나의 원소만을 가지고 있는 배열들이 생기는데, 이 배열들은 피봇으로 계속 순서대로 나눈 것이니, 그대로 이어 붙이면 정렬된 배열을 얻을 수 있다.
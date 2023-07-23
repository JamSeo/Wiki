# 힙(Heap)
데이터에서 **최댓값**과 **최솟값**을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)  
<br>

![heap](https://velog.velcdn.com/images%2Fyanghl98%2Fpost%2Fb898faf5-7394-4dcd-96ee-d043d6f8c139%2Fimage.png)  

부모 노드의 인덱스는 1로, 왼쪽 자식 노드부터 2, 3 순서이다.  

    Parent index  = Children index // 2  
    left child index = Parent index * 2  
    right child index = Parent index * 2 + 1
<br><br>

## 힙을 왜 사용하나요?

최솟값이나 최댓값을 찾기 위해 배열을 사용하면 `Ο(n)`만큼 시간이 걸린다. 하지만 힙을 사용하면 `O(logn)`만큼 소요되므로, 배열을 사용할 때보다 빠르게 최솟값과 최댓값을 구할 수 있다.  

우선순위 큐와 같이 최댓값 또는 최솟값을 빠르게 찾아야하는 알고리즘 등에 활용된다.  
<br>

정리하자면, 힙은 다음 조건을 만족하는 자료구조이다.  

1. 힙은 **최대힙(Max heap)** 과 **최소힙(Min heap)** 으로 나뉘어진다.  최대힙은 자식 노드보다 부모 노드의 값이 크고, 최소힙은 자식 노드보다 부모 노드의 값이 작다.  

2. 노드가 왼쪽부터 채워지는 **완전 이진 트리** 형태를 가진다.  

3. 중복을 허용한다.  

![최대힙, 최소힙](https://velog.velcdn.com/images/gnwjd309/post/6be4941d-5dfc-49ea-8ca3-833fcb690422/image.png)  
<br>

### 힙의 활용 예시
- 시뮬레이션 시스템
- 네트워크 트래픽 제어
- 운영 체제에서의 작업 스케쥴링
- 수치 해석적인 계산


### 완전 이진 트리(Complete Binary Tree)란?

이진 트리에 노드를 삽입할 때 왼쪽부터 차례대로 삽입하는 트리이다. 위 그림과 같이 나타내며, 왼쪽이 비어있고 오른쪽이 채워져 있는 형태는 완전 이진 트리라고 할 수 없다.  
<br><br>

## 힙 vs 이진 탐색 트리

### 이진 탐색 트리(Binary Search Tree)란?
이진 탐색과 연결리스트(linked-list)를 결합한 자료구조의 일종이다.  
이진 탐색의 효율적인 탐색 능력을 유지하면서 빈번한 자료의 입력과 삭제를 가능하도록 한다.  
각 노드에서 왼쪽의 자식 노드는 해당 노드보다 작은 값으로, 오른쪽의 자식 노드는 해당 노드보다 큰 값으로 이루어져 있다.  
<br>

### 공통점
모두 완전 이진 트리이다.  
<br>

### 차이점
- (최대힙의 경우) 힙은 각 노드의 값이 자식 노드보다 크거나 같다.  
- 이진 탐색 트리는 각 노드의 왼쪽 자식은 더 작은 값으로, 오른쪽 자식은 더 큰 값으로 이루어져있다.  
`왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드`  
- 힙은 왼쪽 노드의 값이 크든 오른쪽 노드의 값이 크든 상관 없다.  
- 힙은 최대/최소 검색을, 이진 탐색 트리는 탐색을 위한 구조이다.  

![최대힙, 이진탐색트리](https://velog.velcdn.com/images/gnwjd309/post/7a1ec521-ae89-42de-87e6-14563840bf18/image.png)  
<br><br>

## 힙의 동작

### 힙의 삽입
1. 힙에 새로운 요소가 들어오면, 일단 새로운 노드를 **힙의 마지막 노드에 삽입**한다.  

2. 새로운 노드를 부모 노드들과 교환한다.  

![힙의 삽입](https://velog.velcdn.com/images%2Fyanghl98%2Fpost%2F73220cd3-a136-4ada-8234-91c26f9199ee%2Fimage.png)  

```python
// 최대 힙 삽입
void insert_max_heap(int x) {
    
    maxHeap[++heapSize] = x; // 힙 크기를 하나 증가하고, 마지막 노드에 x를 넣음
    
    for( int i = heapSize; i > 1; i /= 2) {
        
        // 마지막 노드가 자신의 부모 노드보다 크면 swap
        if(maxHeap[i/2] < maxHeap[i]) {
            swap(i/2, i);
        } else {
            break;
        }
        
    }
}
```  
<br>

### 힙의 삭제
1. 최대 힙에서 최대값은 루트 노드이므로 **루트 노드**가 삭제된다. (최대 힙에서 삭제 연산은 최대값 요소를 삭제하는 것)

2. 삭제된 루트 노드에는 **힙의 마지막 노드를 가져옴**

3. 힙을 재구성

![힙의 삭제](https://velog.velcdn.com/images%2Fyanghl98%2Fpost%2Ff33d8046-50c6-4684-8c6c-0ccd687b4211%2Fimage.png)

```python
// 최대 힙 삭제
int delete_max_heap() {
    
    if(heapSize == 0) // 배열이 비어있으면 리턴
        return 0;
    
    int item = maxHeap[1]; 		// 루트 노드의 값을 저장
    maxHeap[1] = maxHeap[heapSize]; 	// 마지막 노드 값을 루트로 이동
    maxHeap[heapSize--] = 0; 		// 힙 크기를 하나 줄이고 마지막 노드 0 초기화
    
    for(int i = 1; i*2 <= heapSize;) {
        
        // 마지막 노드가 왼쪽 노드와 오른쪽 노드보다 크면 끝
        if(maxHeap[i] > maxHeap[i*2] && maxHeap[i] > maxHeap[i*2+1]) {
            break;
        }
        // 왼쪽 노드가 더 큰 경우, swap
        else if (maxHeap[i*2] > maxHeap[i*2+1]) {
            swap(i, i*2);
            i = i*2;
        }
        // 오른쪽 노드가 더 큰 경우, swap
        else {
            swap(i, i*2+1);
            i = i*2+1;
        }
    }
    
    return item;
    
}
```
<br><br>

## 힙의 구현

### heapq 모듈
파이썬 heapq 모듈은 최소 힙을 지원하는 모듈로 직접 최소 힙을 구현하지 않아도 되는 장점이 있어서 소개해드리겠습니다^_^   
<br>

### 데이터 추가
```python
import heapq

heapq.heappush(result, 14)
print(result)
# [14]

heapq.heappush(result, 10)
print(result)
# [10, 14]

heapq.heappush(result, 6)
print(result)
# [6, 14, 10]

heapq.heappush(result, 8)
print(result)
# [6, 8, 10, 14]
```
<br>

### 데이터 삭제
최소, 최대 힙에서 데이터 삭제는 루트 노드를 삭제하는 것이 일반적이라 설명한 것처럼 heapq에서는 루트노드만 삭제할 수 있습니다.  

```python
heapq.heappop(result)
print(result)
# [8, 10, 14]
```
<br>

### 리스트 변환
기존 리스트를 최소 힙으로 변환은 다음과 같이 진행합니다.  

```python
_list = [14, 10, 6, 8, 12, 4]
heapq.heapify(_list)
print(_list)
# [4, 8, 6, 10, 12, 14]
```
<br>

### 최대힙 표현하기
heapq는 최소 힙만 지원하기 때문에 최대 힙을 만드려면 입력 값들에 음수를 씌우면 됩니다.  

```python
max_heap = list(map(lambda x: x*-1, _list))
heapq.heapify(max_heap)
max_heap = list(map(reverse_sign, max_heap))

# [14, 12, 6, 8, 10, 4]
```
<br>

### 힙 정렬
눈치 채셨겠지만 heapq 모듈로 정렬도 가능합니다.  
sorted()라는 좋은 정렬 함수가 내장되어 있지만 꼭 힙 정렬만 구현해야 한다면 아래와 같이 간단하게 구현을 할 수 있습니다.  

```python
import heapq

_list = [14, 10, 6, 8, 12, 4]
heapq.heapify(_list)

method1 = []

while _list:
    method1.append(heapq.heappop(_list))
print(method1)
# [4, 6, 8, 10, 12, 14]
```


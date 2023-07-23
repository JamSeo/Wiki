# 이진 탐색 트리(BST: binary search tree)

이진탐색트리란 이진탐색(binary search)과 연결리스트(linked list)를 결합한 자료구조의 일종이다.    
이진탐색의 효율적인 탐색 능력을 유지하면서도, 빈번한 자료 입력과 삭제를 가능하게끔 고안됐다.   

이진탐색의 경우 탐색에 소요되는 계산복잡성은 O(logn)으로 빠르지만 자료 입력, 삭제가 불가능하다.   연결리스트의 경우 자료 입력, 삭제에 필요한 계산복잡성은 O(1)로 효율적이지만 탐색하는 데에는 O(n)
의 계산복잡성이 발생한다. 두 마리 토끼를 잡아보자는 것이 이진탐색트리의 목적이다.  

이진탐색트리는 다음과 같은 속성을 지니며 아래 그림과 같다.  

![이진탐색트리](https://i.imgur.com/nCYjtI7.png)  

- 각 노드의 왼쪽 서브트리에는 해당 노드의 값보다 작은 값을 지닌 노드들로 이루어져 있다.

- 각 노드의 오른쪽 서브트리에는 해당 노드의 값보다 큰 값을 지닌 노드들로 이루어져 있다.

- 중복된 노드가 없어야 한다.

- 노드의 오른쪽 서브트리에는 그 노드의 값보다 큰 값들을 지닌 노드들로 이루어져 있다.  

- 좌왼쪽 서브트리, 오른쪽 서브트리 또한 이진탐색트리이다.
<br><br>


## 이진 탐색 트리에서의 삽입

이진 탐색 트리의 삽입은 다음과 같은 과정을 거친다.  

1. 삽입할 숫자가 현재 노드 값보다 작다면 왼쪽으로 간다.

2. 삽입할 숫자가 현재 노드 값보다 크다면 오른쪽으로 간다.

3. 자식노드가 없을 때까지 1~2과정을 반복하고 자식노드가 없을 때 만들어서 연결시켜준다.  
<br><br>


## 이진 탐색 트리에서의 검색

이진 탐색 트리의 탐색은 다음과 같은 과정을 거친다.

1. 루트 노드의 키와 찾고자 하는 값을 비교한다. 찾고자 하는 값이라면 탐색을 종료한다.  

2. 찾고자 하는 값이 루트 노드의 키보다 작다면 왼쪽 서브 트리로 탐색을 진행한다.  

3. 찾고자 하는 값이 루트노드의 키보다 크다면 오른쪽 서브트리로 탐색을 진행한다. 

4. 찾고자 하는 값을 찾을 때까지 1~3과정을 반복하고, 만약 값이 존재하지 않으면 NULL을 리턴한다.   

    ![이진 탐색 트리에서의 검색](https://blog.kakaocdn.net/dn/pEBxn/btq9ReoXZUX/7zobmK5yQPPupKqGRgdHcK/img.png)  

### 이진 탐색 트리 삽입, 탐색 소스 코드

```python
class Node:
    def __init__(self, value):
        # double linked list
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head  # 루트노드

    # 삽입
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:              # 이미 가지고 있다면
                    self.current_node = self.current_node.left  # 비교대상을 바꾼다.
                else:
                    self.current_node.left = Node(value)        # 없다면 새로 만들어 연결시킨다.
                    break
            else:
                if self.current_node.right != None:             # 이미 가지고 있다면
                    self.current_node = self.current_node.right # 비교대상을 바꾼다.
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 트리 출력
    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:            # 찾았다
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left  # 비교대상 바꾸기
            else:
                self.current_node = self.current_node.right # 비교대상 바꾸기

        return False                                        # 다 찾아봤는데 없다.
```  
<br><br>


## 이진 탐색 트리에서의 삭제

이진 탐색 트리의 삭제는 어렵기 때문에 경우를 나눠서 생각해본다.  
<br>

### 1) Leaf Node를 삭제
: 해당 노드를 단순히 삭제한다.  
 parent node가 삭제할 노드를 가르키지 않도록 한다.  

![Leaf Node를 삭제](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FqMrWc%2Fbtq7P7Slq4l%2FlRkicc6hxj1orWDDpluR5K%2Fimg.png)  
<br>

### 2) Child Node가 1개인 Node를 삭제
 : 해당 노드를 삭제하고 그 위치에 해당 노드의 자식노드를 대입한다.  
 삭제할 노드의 Parent Node가 삭제할 Node의 child Node를 가르키도록 한다.  

 ![Child Node가 1개인 Node를 삭제](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdwg5Un%2Fbtq7Nx5jN0d%2FLh5FxDewXXbsgzzftV4gd0%2Fimg.png)
<br>

### 3) Child Node가 두개인 Node 삭제 **(중요!)**
: 삭제할 Node의 오른족 자식 중, 가장 작은값을 Parent Node가 가리키도록한다.  

: 또는 삭제할 노드의 왼쪽 자식 중, 가장 큰값을 Parent Node가 가리키도록한다.  

![Child Node가 두개인 Node 삭제](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQvawq%2Fbtq7Q9vdTdF%2F5egBwdal3finEfZIY0tSwk%2Fimg.png)    
<br><br>


## 이진 탐색 트리의 시간 복잡도와 단점

### 시간 복잡도

: 노드가 N개 일때 트리의 높이 h = logN이다.

: 즉, 이진 탐색트리의 시간복잡도는 O(logN)으로 리스트에서 탐색할시에는 O(N)이 걸리는 것에 비해 빠르게 처리가능하다.  
<br>

### 단점

: O(logN)은 트리가 균형잡혀있을 때의 평균 시간복잡도이다.

: 아래 그림과 같이 root node를 잘못잡아서 트리가 불균형이 되어 최악의 경우, linked list와 동일한 성능을 보일 수 있다.

![단점](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FU1glI%2Fbtq7PM8MjSe%2FiKMvziN6xWY2XiEkN2kuM0%2Fimg.png)
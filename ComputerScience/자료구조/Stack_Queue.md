# 스택(Stack)과 큐(Queue)

## 소개
스택(Stack)과 큐(Queue)는 데이터를 임시 저장하기 위해 사용하는 자료구조이며, 데이터를 입력하고 출력하는 방향이 정해져 있다는 점이 서로 비슷하다.
<br>  

---  
<br>

## 스택(Stack)
<br>

![stack](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbmlHbt%2FbtrnjHxkal4%2FMCvYE5QEcgfbtZhXM0cJb0%2Fimg.png)

스택은 **후입선출(LIFO, Last In First Out)** 방식의 자료구조이다.

'후입선출(LIFO)'은 말그대로 나중에 들어온 데이터가 먼저 나가는 방식이며 박스 쌓기에 비유할 수 있다.  

흔히 박스는 아래에서부터 위로 차곡차곡 쌓고 박스를 치울 때는 위에 있는 박스부터 내리는 것과 같다.  
<br><br>

### 스택(Stack)의 특징

- 스택 내부의 데이터는, `top`을 통해서만 접근할 수 있다. *`top`은 가장 최근(마지막)에 들어온 자료를 의미한다.*  

- 스택에 데이터를 삽입할 때는, top 위에 쌓게 된다. (**push**)  

- 스택에서 데이터를 삭제할 때는, top 에 위치한 데이터를 삭제하게 된다. (**pop**)  
<br><br>

### 스택(Stack)의 장단점

- `top`을 통해 접근하기 때문에 데이터 접근, 삽입, 삭제가 빠르다.  

- `top` 위치 이외의 데이터에 접근할 수 없기 때문에 탐색이 불가능하다. 탐색하려면 모든 데이터를 꺼내면서 진행해야 한다.  
<br><br>

### 스택(Stack)의 활용 예시

- 웹 브라우저 방문기록(뒤로 가기)  
    가장 마지막에 열린 페이지부터 다시 보여준다.  

- 실행 취소(undo)  
    가장 마지막에 실행된 것부터 실행을 취소한다.  

- 역순 문자열 만들기  
    가장 마지막에 입력된 문자부터 출력한다.  

- 후위 표기법 계산  

- 수식의 괄호 검사  
    연산자 우선순위 표현을 위한 괄호 검사  

- 재귀 알고리즘   

- 깊이 우선 탐색(DFS, Depth-First Search)  
<br>

---
<br>

## 큐(Queue)
<br>

![queue](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FboPAln%2FbtrnfBrlYFt%2FNRNKLJXH4DqqZgi2ieqhZ0%2Fimg.png)

큐는 **선입선출(FIFO, First In FirstOut)** 방식의 자료구조이다.  

선입선출(FIFO)은 말그대로 먼저 들어온 데이터가 먼저 나가는 방식이며 대기 줄에 비유할 수 있다.  

흔히 우리가 놀이기구 줄을 설 때 먼저 온 사람이 먼저 타는 것과 같다.  
<br><br>

### 큐(Queue)의 특징

- 스택은, top 을 통해서만 삽입, 삭제가 이루어졌었다. 하지만 큐는 삽입, 삭제가 다른 방향에서 이루어진다.  

- 이때, 삭제 연산만 수행되는 곳을 **프론트(front)**, 삽입 연산만 수행되는 곳을 **리어(rear)** 라고 한다.  

- 프론트(front)에서 이루어지는 삭제 연산을 **디큐(dnQueue)** 라고 하며, 리어(rear)에서 이루어지는 삽입 연산을 **인큐(enQueue)** 라고 한다.  

- 데이터를 삭제하기 전에는 큐가 empty 한지, 큐에 데이터를 추가하려 할 때는 큐가 full 인지 확인 후 진행해야 한다.  
<br><br>  

### 큐(Queue)의 구현 방법
<br> 

#### 1. 리스트 자료형

리스트를 사용하면 큐에 데이터를 넣는 enqueue를 `append()` 메소드, 데이터를 빼는 dequeue를 `pop(0)`로 구현할 수 있다.  

다만 리스트의 pop(0)은 O(n)의 시간복잡도를 가지기 때문에 큐를 구현할 때는 더 효율적인 방법을 사용한다.  
<br>

#### 2. Queue

**queue 모듈의 Queue**는 데이터를 단방향에서 추가하고 제거할 수 있는 자료구조이다.   

enqueue를 위해서는 `put()` 메소드를 , dequeue를 위해서는 `get()` 메소드를 사용한다.  

get() 메소드는 리스트의 pop()과 다르게 시간복잡도가 O(1)이므로 리스트보다 더 효율이 좋다.  
<br>

#### 3. 덱(deque)

**collections 모듈의 deque**는 double - ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조이다.  

deque는 양방향이기 때문에 `append(), pop()`과 더불어 `appendleft(), popleft()` 메소드가 있어 각각 맨 앞에 데이터를 삽입하거나 맨 앞에서 제거할 수 있다.  

appendleft(), popleft() 메소드는 각각 시간복잡도가 O(1)이기 때문에 리스트보다 더 효율적이다.  

일반적으로는 양방향을 지원하고 효율이 좋은 deque를 이용하여 큐를 구현한다.  
<br><br>  

### 선형 큐(Linear Queue)
<br>

![선형큐](https://velog.velcdn.com/images%2Fnnnyeong%2Fpost%2Fd185914f-c33a-4d02-8a92-1a4720635ce0%2Fimage.png)

- 선형 배열을 사용하여 구현된 큐  

- 삽입을 위해서는 계속해서 요소들을 이동시켜야 함  

- `front, rear` 는 증가만 하는 방식, 실제로 front 앞쪽에 공간이 있더라도 삽입할 수 없는 경우가 발생할 수 있음
<br><br>

### 원형 큐(Circular Queue)
<br>

![원형큐](https://velog.velcdn.com/images%2Fnnnyeong%2Fpost%2Ff439a687-709e-40cf-90c9-55206e834652%2Fimage.png)

- 선형 큐의 단점을 보완  

- front = 맨 첫번째 요소 바로 앞을 가리킴  

- rear = 마지막 요소 가리킴  

- 큐 empty 상태 : front == rear  

- 큐 full 상태 : front == (rear+1) % MAX_QUEUE_SIZE  

- 공백 상태와 포화 상태를 구분하기 위해 하나의공간을 비워둠  
<br><br>  

### 큐(Queue)의 활용예시

- 프로세스 관리  

- 너비 우선 탐색(BFS, Breadth-First Search)  

- 캐시(Cache) 구현  

- 대기 순서 관리  

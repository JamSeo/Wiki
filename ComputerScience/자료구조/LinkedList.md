# Linked List

## 소개
Linked List는 Array List와는 다르게 엘리먼트와 엘리먼트 간의 연결(link)을 이용해서 리스트를 구현한 것을 의미합니다. 그래서 이름도 linked list입니다.<br>  

좀더 쉬운 이해를 위해 Array List의 성질에 대해 다시 한번 짚어드리겠습니다.^_^  
서로 무엇이 다른지 생각하면서 읽으시면 이해하시기 쉬울겁니다 ㅎㅎ

"Array List의 성질"

 1. 초기 선언시 크기 지정 필요 (크기 지정 누락시 컴파일에러 발생)
 2. 초기 선언시 변수의 자료형 지정 필요
 3. 하나의 배열 안에 서로 다른 자료형 데이터를 저장할 수 없음.  

<br>  

---  
<br>

## 메모리 구조
연결에 대해서 알아보기에 앞서 메모리 구조에 대해서 조금 살펴보겠습니다.  
메모리는 건물에 비유할 수 있을 것 같습니다. 아래 그림은 배열을 사용하는 것과 Linked list를 사용하는 것을 비유해서 보여주고 있습니다. 여러분의 회사가 한 건물의 일부를 임대해서 사용한다고 생각해주세요.  

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2903.png)  
<br>

### Array List
첫 번째 회사는 모든 직원이 같은 층의 사무실에 모여있습니다. 배열은 건물을 이런 식으로 사용하는 것과 비슷합니다. 만약 회사가 성장해서 사무실이 좁아지면 더 이상 새로운 직원을 뽑을 수 없습니다. 붙어있는 공간이 없기 때문이죠.  
<br>

### Linked List  
![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2928.png)  

두 번째 회사는 한 건물 안에서 사무실이 서로 떨어져 있습니다. 덕분에 직원이 늘어도 큰 걱정이 없습니다. 건물에서 비어있는 곳 아무데나 임대해서 들어가면 되니까요.  
그런데 방문자가 사무실을 찾는 방법이 좀 비효율적입니다. 위의 그림에 있는 방문자가 3번째 사무실을 찾아가려면 우선 첫 번째 화살표의 사무실을 찾아가야 합니다. 이 사무실의 직원에게 다음 사무실이 어딘지 물어봅니다. 그럼 알려주는 사무실로 이동 한 후에 다시 물어봐서 그다음 사무실로 이동합니다.  
<br>

---
<br>

## 연결
Linked list의 이름에 왜 연결을 의미하는 링크가 사용되었는지 짐작할 수 있겠죠? 배열과는 다르게 Linked list는 그 위치가 흩어져 있기 때문에 서로 연결되어 있어야 합니다. 바로 그런 점에서 연결이라는 이름을 갖게 된 것입니다.

용어를 정리해봅시다.  
Array list에서는 엘리먼트라는 이름을 사용했지만 Linked list와 같이 연결된 엘리먼트들은 `노드(node, 마디, 교점의 의미)` 혹은 `버텍스(vertex, 정점, 꼭지점의 의미)`라고 부릅니다. 이런 용어들은 연결성이 강조된 표현이라고 생각하시면 됩니다. 여기서도 엘리먼트, 노드, 버텍스를 혼용해서 사용하도록 하겠습니다.  
<br>

---
<br>

## 구조
그럼 Linked list의 구조를 알아봅시다. 리스트는 노드(엘리먼트)들의 모임입니다. 따라서 내부적으로 노드를 가지고 있어야 합니다. Array list의 경우 엘리먼트가 배열의 엘리먼트였습니다. Linked list는 배열과 다른 구조를 사용합니다.

노드는 최소한 두 가지 정보를 알고 있어야 합니다.  
노드의 값과 다음 노드입니다. 각각의 노드가 다음 노드를 알고 있기 때문에 하나의 연결된 값의 모임을 만들 수 있는 것입니다. 아래 그림은 Linked list의 구조를 보여줍니다.  

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2939.png)  

이것을 구현하는 방법은 여러가지입니다. 만약 사용 언어가 C라면 구조체, Java와 같은 객체지향 언어라면 객체에 데이터 필드와 링크 필드를 만듭니다.  

보통 데이터 필드는 `value`라는 이름의 변수, 링크 필드는 `next` 변수를 사용합니다. value에는 노드의 값이 저장되고, next에는 다음 노드의 포인터나 참조값을 저장해서 노드와 노드를 연결시키는 방법을 사용합니다.

### Head
위의 그림을 보면 head라는 것이 있습니다. 건물의 비유를 다시 사용해보죠.  
건물에 들어가려면 출입문을 찾아야 합니다. 리스트를 하나의 건물로 비유하자면 출입문에 해당하는 것이 Head입니다. Linked list를 사용하기 위해서는 이 Head가 가리키는 첫번째 노드를 찾아야 합니다.  
<br>

---
<br>

## 데이터의 추가

### 시작부분에 추가
노드를 첫 번째 위치에 추가해봅시다.  
<br>
1. 우선 새로운 노드를 생성합니다.  
    ```
    Vertex temp = new Vertex(input)
    ```  
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2943.png)  
<br>

2. 새로운 노드의 다음 노드로 첫번째 노드를 가리킵니다.  
    ```
    temp.next = head
    ```  
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2944.png)  
<br>

3. 새로 만들어진 노드가 첫번째 노드가 되도록 head의 값을 변경합니다.  
    ```
    head = temp
    ```  
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2945.png)   
<br>

### 중간에 추가

3번째 자리(inx=2)에 90을 추가해봅시다.

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2930.png)  
3번째 자리는 붉은 화살표가 표시된 부분입니다. 즉 6과 23 사이에 90을 위치시키는 것이 우리가 하려는 것입니다. 우선 3번째 자리를 찾아야 합니다.  
<br>

1. Head를 참조해서 첫 번째 노드를 찾습니다.  
    ```
    Vertex temp1 = head
    ```   
<br>

2. 23의 자리에 새로운 노드를 위치시키기 위해서는 6을 알고 있어야 합니다. 6의 next로 새로운 노드를 지정해야 하기 때문이죠. 아래는 6을 temp1으로 지정하기 위한 반복문입니다.  
    ```
    //현재 k의 값은 2

    while (--k!=0)
      temp1 = temp1.next
    ```  
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2920.png)  
<br>

3. 6의 next를 이용해서 23을 찾아서 temp2로 지정합니다.  
    ```
    Vertex temp2 = temp1.next
    ```  
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2921.png)  
<br>

4. 값이 90인 새로운 노드를 생성하고, 6의 next 노드로 지정합니다.
    ```
    Vertex newVertex = new Vertex(input)
    temp1.next = newVertex
    ```  
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2923.png)  
<br>

5. 새로운 노드의 next 노드로 23번을 지정합니다. 이렇게 해서 90을 3번째 자리에 위치시켰습니다.  
    ```
    newVertex.next = temp2
    ```  
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2924.png)  
<br>

---
<br>

## 데이터의 제거
데이터 제거는 추가 과정과 비슷합니다. 아래 리스트에서 세번째 노드(idx=2)를 제거하는 과정을 알아봅시다.  

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2932.png)  
<br>

1. 우선, Head에 접근해서 세번째 노드를 찾습니다.  

    ```
    Vertex cur = head 
    //k = 2
    while (--k!=0)
      cur = cur.next
    Vertex tobedeleted = cur.next
    ```
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2934.png)  
<br>

2. 두 번째 노드의 next를 23으로 변경합니다. 이제 90을 지웁니다.
    ```
    cur.next = cur.next.next
    ```
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2935.png)  
<br>

3. 90을 삭제해서 메모리에서 제거합니다.
    ```
    delete tobedeleted
    ```
    ![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2936.png)  
<br>

---
<br>

## 인덱스를 이용한 데이터 조회

### Linked List
인덱스를 이용해서 데이터를 조회할 때 Linked list는 Head가 가리키는 노드부터 시작해서 순차적으로 노드를 찾아가는 과정을 거쳐야 합니다. 만약 찾고자 하는 엘리먼트가 가장 끝에 있다면 모든 노드를 탐색해야 합니다.  

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2937.png)  
<br>

### Array List
반면에 Array를 이용해서 리스트를 구현하면 인덱스를 이용해서 해당 엘리먼트에 바로 접근 할 수 있기 때문에 매우 빠릅니다.  

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2938.png)  
<br>

---
<br>

## 정리

### 왜 Linked List를 사용하나?

배열은 비슷한 유형의 선형 데이터를 저장하는데 사용할 수 있지만 제한 사항이 있습니다.

1. 배열의 크기가 고정되어 있어 미리 요소의 수에 대해 할당을 받아야 함  

2. 새로운 요소를 삽입하는 것은 비용이 많이 듬 (공간을 만들고, 기존 요소 전부 이동)  
<br>

### 장점

1. 동적 크기  

2. 삽입/삭제 용이  
<br>

### 단점

1. 임의로 액세스를 허용할 수 없음. 즉, 첫 번째 노드부터 순차적으로 요소에 액세스 해야함. (이진 검색 수행 불가능)

2. 포인터의 여분의 메모리 공간이 목록의 각 요소에 필요


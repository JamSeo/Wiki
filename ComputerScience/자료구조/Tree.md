# 트리(Tree)
트리 (Tree)란 노드들이 나무 가지처럼 연결된 비선형 계층적 자료구조입니다.  
마치 나무를 거꾸로 뒤집어 놓은 모양과 유사합니다.  

![트리.png](https://blog.kakaocdn.net/dn/eeoNuG/btq1Eo7t7Xk/0bPk7BzhiruKSsgtiubvK0/img.png)  
<br>

트리는 또한 트리 내에 다른 하위 트리가 있고 그 하위 트리 안에는 또 다른 하위 트리가 있는 재귀적 자료구조이기도 합니다.  

컴퓨터의 direcory구조가 트리 구조의 대표적인 예가 될 수 있습니다.  

![컴퓨터구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbl6Ecy%2Fbtq1yFCmshK%2F4uvfvvAxqX3TYlEN2P2eX1%2Fimg.png)  
<br><br>

## 트리 구조에서 사용되는 기본 용어
<br>

![트리용어](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcA6btV%2Fbtq1z5fVwht%2F96SGFKq5O3QtaUBabJKibK%2Fimg.png)  

### 노드(Node)
- 트리를 구성하는 기본 요소
- 노드에는 Key( 또는 Value)와 하위 노드에 대한 포인터가 있습니다.

### 간선(Edge)
- 노드와 노드 간의 연결선

### 루트 노드(Root Node)
- 트리 구조에서 부모가 없는 최상위 노드

### 부모 노드 (Parent Node)
- 자식 노드를 가진 노드

### 자식 노드 (Child node)
- 부모 노드의 하위 노드

### 형제 노드 (Sibling node)
- 같은 부모를 가지는 노드

### 깊이 (depth)
- 루트에서 어떤 노드까지의 간선(Edge) 수
- 루트 노드의 깊이 : 0
- D의 깊이 : 2

### 높이 (height)
- 어떤 노드에서 리프 노드까지 가장 긴 경로의 간선(Edge) 수
- 리프 노드의 높이 : 0
- A 노드의 높이 : 3  
<br><br>  

## 트리의 특징
1. 트리에는 사이클이 존재할 수 없다. (만약 사이클이 만들어진다면, **그것은 트리가 아니고 그래프!!**)  

2. 모든 노드는 자료형으로 표현이 가능하다.  

3. 루트에서 한 노드로 가는 경로는 유일한 경로 뿐이다.  

4. 노드의 개수가 N개면, 간선은 N-1개를 가진다.  

5. 가장 중요한 것은, 그래프와 트리의 차이가 무엇인가인데, 이는 사이클의 유무로 설명할 수 있다.  
<br><br>

## 트리 순회 방식
트리를 순회하는 방식은 총 4가지가 있다. 아래 그림을 예시로 진행해보겠습니다.  

![트리 순회](https://camo.githubusercontent.com/78163ac30efb3626bee26e7269938859caec33b6def337ff7657046122bb78ff/68747470733a2f2f7777772e6765656b73666f726765656b732e6f72672f77702d636f6e74656e742f75706c6f6164732f62696e6172792d747265652d746f2d444c4c2e706e67)
<br>

### 전위 순회(pre-order)
각 루트(Root)를 순차적으로 먼저 방문하는 방식  

(Root → 왼쪽 자식 → 오른쪽 자식)  

    1 → 2 → 4 → 8 → 9 → 5 → 10 → 11 → 3 → 6 → 13 → 7 → 14  
<br>

### 중위 순회(in-order)
왼쪽 하위 트리를 방문 후 루트(Root)를 방문하는 방식  

(왼쪽 자식 → Root → 오른쪽 자식)  

    8 → 4 → 9 → 2 → 10 → 5 → 11 → 1 → 6 → 13 → 3 →14 → 7  
<br>

### 후위 순회(post-order)
왼쪽 하위 트리부터 하위를 모두 방문 후 루트(Root)를 방문하는 방식  

(왼쪽 자식 → 오른쪽 자식 → Root)  

    8 → 9 → 4 → 10 → 11 → 5 → 2 → 13 → 6 → 14 → 7 → 3 → 1  
<br>

### 레벨 순회(level-order)
루트(Root)부터 계층 별로 방문하는 방식  

    1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 13 → 14  
<br><br>

## 트리 종류

### 편향 트리 (skew tree)
모든 노드들이 자식을 하나만 가진 트리  
왼쪽 방향으로 자식을 하나씩만 가질 때 left skew tree, 오른쪽 방향으로 하나씩만 가질 때 right skew tree라고 합니다.  
<br>

### 이진트리 (Binary Tree)
각 노드의 차수(자식 노드)가 2 이하인 트리  
<br>

### 이진 탐색 트리 (Binary Search Tree, BST)
순서화된 이진 트리  
노드의 왼쪽 자식은 부모의 값보다 작은 값을 가져야 하며 노드의 오른쪽 자식은 부모의 값보다 큰 값을 가져야 합니다.  
<br>

### m 원 탐색 트리(m-way search tree)
최대 m개의 서브 트리를 갖는 탐색 트리  
이진 탐색 트리의 확장된 형태로 높이를 줄이기 위해 사용합니다.  
<br>

### 균형 트리 (Balanced Tree, B-Tree)
m원 탐색 트리에서 높이 균형을 유지하는 트리  
height-balanced m-way tree라고도 합니다.  
아래는 '균형 이진 트리'. 모든 노드의 왼쪽과 오른쪽 하위 트리의 높이가 최대 1만큼 차이가 날 수 있는 이진 트리입니다.  

![균형 이진 트리](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbxe2sR%2FbtqEUEMeslx%2Fzk0a36hjtoMRuRAAB6rvBK%2Fimg.png)  

<br><br>

## 트리 사용 사례

### 계층적 데이터 저장
트리는 데이터를 계층 구조로 저장하는 데 사용됩니다.   
예를 들어 파일 및 폴더는 계층적 트리 형태로 저장됩니다.  
<br>

### 효율적인 검색 속도
효율적인 삽입, 삭제 및 검색을 위해 트리 구조를 사용합니다.  
<br>

### 힙(Heap)
힙도 트리로 된 자료 구조입니다.  
<br>

### 데이터 베이스 인덱싱
데이터베이스 인덱싱을 구현하는데 트리를 사용합니다.  
  예) B-Tree, B+Tree, AVL-Tree..  
<br>

### Trie
사전을 저장하는 데 사용되는 특별한 종류의 트리입니다.  
# 트라이(Trie)


## 트라이(Trie) 자료구조란?
트라이(Trie)는 문자열의 집합을 표현하는 `트리 자료구조`이다.   
원하는 원소를 찾기 위해 자주 이용되는 이진 검색 트리에서는 원소를 찾는데 O(logN)의 시간이 걸린다.  
하지만, 문자열의 경우 두 문자열을 비교하기 위해서는 문자열의 길이(M)만큼의 시간이 걸리기 때문에 원하는 문자열을 찾기 위해서는 O(MlogN)의 시간이 걸리게 된다.  
따라서 여러 번 이 작업을 수행한다면 시간이 오래 걸릴 것이다.  

이 단점을 해결하기 위한 문자열 특화 자료구조가 트라이(Trie)이다.  

쉽게 말해, `"문자열을 빠르게 탐색할 수 있는 자료구조"`이다.  
<br>


## 트라이(Trie) 작동원리

다음 그림은 문자열 집합 {"rebro", "replay", "hi" , "high", "algo"} 를 트라이로 구현한 것이다.  

![트라이 이미지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FpYAoN%2FbtqPZJ9d7rl%2FYGhdbBzRXzLdY1ytJmsvJK%2Fimg.png)

이처럼, 트라이는 집합에 포함된 문자열의 접두사들에 대응되는 노드들이 서로 연결된 트리이다.  
한 문자열에서 다음에 나오는 문자가 현재 문자의 자식 노드가 되고, 빨간색으로 나타낸 노드는 문자열의 끝을 의미한다.  
그렇다면 트라이 구조가 문자열을 탐색하기 위한 자료구조이므로, 문자열을 탐색하기 위해서는 다음 글자에 해당하는 노드가 연결되어 있는지, 연결되어 있다면 그 노드를 타고 계속해서 따라가야 할 것이다.   
그리고 문자열의 끝에 도달했을 때, 해당 노드에서 끝나는 문자열(빨간 노드)이 있다면 찾고자 하는 문자열이 집합에 포함되어 있는 것이다.  
잘 이해해보면, 문자열의 끝을 나타내는 빨간 노드는 항상 하나의 문자열의 끝을 의미하게 되는 것을 알 수 있다.  

그리고, 트라이의 중요한 속성 중 하나는, 루트에서부터 내려가는 경로에서 만나는 글자들을 모으면 찾고자 하는 문자열의 접두사를 얻을 수 있다는 것이다.   

    예를 들어서 "rebro"를 찾는다고 해보자.  

    r -> re -> reb -> rebr -> rebro가 되므로 "rebro"의 모든 접두사들이 다 구해지게 된다.  

따라서 각 노드에는 접두사를 저장할 필요 없이, 문자 하나만 저장해둬도 충분하게 된다.  
<br>


## 트라이(Trie) 자료구조의 장/단점

트라이의 장점은 앞에서도 언급했듯이 당연히 `문자열을 빠르게 찾을 수 있다는 점`이다.  
더불어, 문자열을 집합에 추가하는 경우에도 문자열의 길이만큼 노드를 따라가거나, 추가하면 되기 때문에  
문자열의 추가와 탐색 모두 O(M)만에 가능하다.  

반면에 트라이의 단점은 필요한 `메모리의 크기가 너무 크다는 점`이다.  
문자열이 모두 영소문자로 이루어져 있다고 해도, 자식 노드를 가리키는 26개의 포인터를 저장해야 한다.  
최악의 경우에는 집합에 포함되는 문자열들의 길이의 총합만큼 노드가 필요하므로, 총메모리는  
`O(포인터 크기 * 포인터 배열 개수 * 총노드의 개수)`가 된다.  
만약, 1000자리의 문자열이 1000개만 들어온다고 하더라도 100만 개의 노드가 필요하고, 포인터의 크기가 8byte라고 하면 약 __200MB의 메모리__ 가 필요하게 된다.   

따라서, 이 단점을 해결하기 위해서 보통 map이나 vector를 이용하여 필요한 노드만 메모리를 할당하는 방식들을 이용하는데, 문제에 따라서 메모리 제한이 빡빡한 경우에는 최적화가 꽤나 까다롭다.  
또한, 문제에서 주어진 조건을 보고 트라이를 이용할 수 있는 문제인지 파악하는 것도 중요하다.  
<br>


## 트라이(Trie) 자료구조의 구현

### Node 구현

```python
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        # self.data = False
        self.data = data
        self.children = {}
```

노드에는 세가지가 필요합니다.

1. key : 값으로 입력될 문자
2. data : 문자열의 종료를 알리는 flag. (True/False로도 구현할 수 있지만, 돌아가는 일이 없게 하기위해 전체 문자열을 저장)
3. children : 자식노드를 저장  
<br>

### Trie 구현

```python
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words
```

Trie 에는 여러가지 함수가 필요합니다.

1. __init__ : head를 빈 노드로 설정
2. __insert__ : 트리를 생성하기 위한 함수. 입력된 문자열의 문자를 하나씩 children에 확인 후 저장하고 문자열을 다 돌면 마지막 노드의 data에 문자열을 저장.
3. __search__  : 문자열이 존재하는지에 대한 여부를 리턴하는 함수. 문자열을 하나씩 돌면서 확인 후 ​마지막 노드가 data가 존재한다면 True, 그렇지 않으면 False를 리턴한다.
4. __starts_with__ : prefix 단어로 시작하는 단어를 찾고 배열로 리턴하는 함수. prefix단어까지 tree를 순회 후 data가 존재하는 것들만 배열에 저장​하여 리턴한다.
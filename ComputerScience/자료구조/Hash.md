# Hash(해시)

## Hash Table(해시 테이블)

해시테이블은 해시함수를 사용하여 key를 해시값으로 매핑하고, 이 해시값을 index로 삼아 데이터를 (Key, Value)의 구조로 저장하는 자료구조이다. 단순하게 key-value로 이루어진 자료구조라고 생각하면 된다. 여기서 실제 값이 저장되는 장소를 버킷 또는 슬롯이라고 한다.

<div align="center">  

![해시테이블](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb1zOw1%2FbtqL6HAW7jy%2FjpBA5pPkQFnfiZcPLakg00%2Fimg.png)
</div>

예를 들어 우리가 ("John Smith", "521-1234")인 데이터를 크기가 16인 해시 테이블에 저장한다고 하자. 그러면 먼저  
(1) index = hash_function("John Smith") % 16 연산을 통해 index 값을 계산한다. 그리고  
(2) array[index] = "521-1234" 로 전화번호를 저장하게 된다.  

이러한 해싱 구조로 데이터를 저장하면 Key값으로 데이터를 찾을 때 해시 함수를 1번만 수행하면 되므로 매우 빠르게 데이터를 저장/삭제/조회할 수 있다. 이때 `해시테이블의 평균 시간복잡도는 O(1)`이다.  
<br><br>



## Hash Function(해시 함수)

해시와 해시테이블을 제대로 알기전에 Hash Function을 알아야 한다. 해시 함수는 Key(Input)를 **고정된 길이**의 Hash(Output)로 변경해주는 역할을 하며, 이 과정을 **hashing**이라고 한다. 이때 도출된 Hash(해시)가 바로 버킷의 저장위치(index)가 된다고 생각하면 된다. 즉 Hash Function는 `key로 해시를 만들어내는 함수`이다.  
<br><br>



## Hash Table의 구성

### key
- 고유한 값, hash function의 Input이 된다.

- key값을 그대로 저장소의 색인으로 사용할 경우 key의 길이만큼의 정보를 저장해야한 공간도 따로 마련해야 하기 때문에(key의 길이가 제각각 일수 있다.), 고정된 길이의 해시로 변경한다.  

### hash function
- key를 고정된 길이의 hash로 변경해주는 역할을 한다.

- **서로 다른 key가 hashing 후 같은 hash값이 나오는 경우가 있다. 이를 해시충돌이라고 한다.** 해시 충돌 발생확률이 적을 수록 좋다.

- 해시 충돌이 균등하게 발생하도록 하는것도 중요하다. 모든 키가 같은 해시값이 나오게 되면 데이터 저장시 비효율성도 커지고 보안이 취약해져서 좋지 않다.

### value
- 저장소(버킷,슬롯)에 최종적으로 저장되는 값으로, hash와 매칭되어 저장되어진다.

### hash table
- 해시함수를 사용하여 키를 해시값으로 매핑하고, 이 해시값을 주소 또는 색인 삼아 (key, value)의 구조로 저장하는 자료구조이다.

- 데이터가 저장되는 곳을 버킷, 슬롯이라고 한다.  
<br><br>



## 장점

- 해시테이블은 key-value가 1:1로 매핑되어 있기 때문에 삽입, 삭제, 검색의 과정에서 모두 평균적으로 O(1)의 시간복잡도를 가지고 있다.  

- 적은 자원으로 많은 데이터를 효율적으로 관리할 수 있기 때문이다.

- 하드디스크나 클라우드에 존재하는 무한에 가까운 데이터(key)들을 유한한 개수의 해시 값으로 매핑함으로써 작은 크기의 캐시 메모리로도 프로세스를 관리할 수 있게 된다.  
<br><br>



## 단점

- 해시 충돌이 발생(개방 주소법, 체이닝 과 같은 기법으로 해결해 줘야 한다.)

- 순서/관계가 있는 배열에는 어울리지 않는다.

- 공간 효율성이 떨어진다. 데이터가 저장되기 전에 저장공간을 미리 만들어놔야한다. 공간을 만들었지만 공간에 채워지지 않는 경우가 발생한다.

- hash function의 의존도가 높다. 해시함수가 복잡하다면 hash를 만들어 내는데 오래 걸릴 것이다.  
<br><br>



## 해시 충돌

만약 A, B 두 개의 key가 있다고 하자. A와 B를 hash function으로 해시 값을 얻었는데 hash값이 2로 똑같이 나왔다. 이런 현상을 hash collision 이라고 한다.  

해시 함수로 해시를 만드는 과정에서 서로 다른 key가 같은 해시로 변경되면 같은 공간에 2개의 value가 저장되므로 key-value가 1:1로 매핑되어야 하는 해시 테이블의 특성에 위배된다. *해시 충돌은 필연적으로 나타날 수 밖에 없다.*  
<br><br>



## 해시 충돌 해결 방법

### 1. Chaining(체이닝)
연결리스트로 노드를 계속해서 추가하는 방식; 모든 자료를 해시테이블에 담는 것  

![chaining](https://user-images.githubusercontent.com/63203480/134490458-c4403dfc-9a08-477f-a3da-f6173b2bfba7.png)  

- 제한 없이 계속 데이터를 연결할 수 있지만, 메모리 문제가 있다.   
<br>

### 2. Open addressing
해시 함수로 얻은 주소가 아닌 다른 주소에 데이터를 저장할 수 있도록 허용하는 방식  

- 예) 해당 키 값에 저장되어 있을 경우 다음 주소에 저장  
<br>

### 3. 선형 탐색
해시 값에 다른 데이터가 이미 저장되어 있을 경우 정해진 고정 폭으로 옮겨 접근하는 방식으로 해시 값의 중복을 피한다.  

![선형탐색](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdObW50%2FbtqS6WR4DDX%2FMMAfztdjaT8fgJ0whFFy0K%2Fimg.png)  

- 52번 해시에서 충복이 일어나 고정폭(1) 씩 건너뛰면서 빈 해시를 찾으려면 57까지 5번의 연산을 해야한다. 특정 해시값 주변 버킷이 모두 채워져 있는 primary clustring 문제에 취약하다.
<br>

### 4. 제곱 탐색
해시 값에 다른 데이터가 이미 저장되어 있을 경우 정해진 고정 폭을 제곱수로 옮겨 접근하는 방식으로 해시 값의 중복을 피한다.

- 고정폭이 아닌 1칸 -> 4칸 -> 9칸 -> 16칸 씩 건너 뛰면서 빈 칸은 찾는다. 공간을 많이 확보해놔야 한다.
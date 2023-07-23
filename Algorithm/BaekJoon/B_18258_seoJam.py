import sys
input = sys.stdin.readline
from collections import deque
# deque를 사용하면 얻는 장점
#
# 엄격한 리스트를 만들 수 있다.
# 속도가 리스트에 비해 굉장히 빠르다. List = O(n), deque = O(1)
# 당연하지만 큐작업이 훨씬 편해진다.

N = int(input())
q = deque([])

for i in range(N):
    temp = input().split()

    if temp[0] == 'push':
        q.append(temp[1])

    elif temp[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif temp[0] == 'size':
        print(len(q))

    elif temp[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif temp[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif temp[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
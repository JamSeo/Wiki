import sys
input = sys.stdin.readline
from collections import deque

def bfs(R):  # R : 시작 정점
    order = 1  # 방문 순서
    visited[R] = order  # 시작 정점 R에 방문(순서) 표시
    q = deque([R])
    q.append(R)  # 큐 맨 뒤에 시작 정점 R을 추가

    while q:
        me = q.popleft()  # 큐 맨 앞쪽의 요소를 삭제
        for near in E[me]:  # E(u) : 정점 u의 인접 정점 집합
            if not visited[near]:
                order += 1
                visited[near] = order  # 정점 v 방문(순서) 표시
                q.append(near)  # 큐 맨 뒤에 정점 v를 추가


N, M, R = map(int, input().split())
E = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(1, N + 1):
    E[i].sort()  # 정점 번호를 오름차순으로 방문하도록

bfs(R)
print(*visited[1:], sep='\n')

import sys
input = sys.stdin.readline
# recursion_limit이 10**6 부터는 메모리초과, 10**4 밑으로는 RecursionError 떠서
# 잔머리 써가면서 10**5로 맞춰주니까 합격했씁니다...후
sys.setrecursionlimit(10**5)

def dfs(R):  # R : 시작 정점
    global order
    order += 1
    visited[R] = order  # 시작 정점 R에 방문(순서) 표시

    for near in E[R]:  # E(u) : 정점 u의 인접 정점 집합
        if not visited[near]:
            dfs(near)


N, M, R = map(int, input().split())
E = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
order = 0

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(1, N + 1):
    E[i].sort()  # 정점 번호를 오름차순으로 방문하도록

dfs(R)
print(*visited[1:], sep='\n')


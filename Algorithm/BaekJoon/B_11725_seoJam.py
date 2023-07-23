from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)

# 트리 구조 정리
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# BFS; 연결된 node 중 방문하지 않은 node를 찾아서 부모 정보를 입력
q = deque([1])
while q:
    parent = q.popleft()
    for child in tree[parent]:
        if not visited[child]:
            visited[child] = parent
            q.append(child)

print(*visited[2::], sep='\n')
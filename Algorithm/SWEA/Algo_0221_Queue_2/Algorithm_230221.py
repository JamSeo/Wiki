# 노드와 간선
V, E = 7, 8
# 시작점
S = 1

# 연결 정보 날 것
connected = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 연결 정보 전처리
map = [[0] * (V + 1) for _ in range(V + 1)]
# 간선 개수 만큼 반복
for i in range(E):
    n1, n2 = connected[i * 2], connected[i * 2 + 1]
    map[n1][n2] = 1

# 방문 체크
visited = [0 for _ in range(V + 1)]

# BFS용 큐, 시작은 S
queue = [S]
visited[S] = 1


while queue:
    now = queue.pop(0)
    print(f'-{now}', end = '')
    # 인접한 애들 찾기
    for next in range(1, V + 1):
        # 연결되어 있고 and 방문한적 없느지?
        if map[now][next] == 1 and visited[next] == 0:
            visited[next] = 1
            queue.append(next)
print()


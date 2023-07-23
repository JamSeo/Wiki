import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    map_ = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        map_[n1][n2] = 1
        map_[n2][n1] = 1

    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    distance = [0] * (V + 1)
    visited[S] = 1
    queue = [S]

    while queue:
        now = queue.pop(0)
        for near in range(1, V + 1):
            if map_[now][near] and not visited[near]:
                queue.append(near)
                visited[near] = 1
                distance[near] = distance[now] + 1

    print(f'#{tc} {distance[G]}')
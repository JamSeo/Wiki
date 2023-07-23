import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    E, S = map(int, input().split())
    temp = list(map(int, input().split()))

    # 비상연락망 만들기
    contact = [[0] * 101 for _ in range(101)]
    for i in range(E // 2):
        from_, to_ = temp[2 * i], temp[2 * i + 1]
        contact[from_][to_] = 1

    q = [S]
    visited = [0] * 101
    visited[S] = 1

    while q:
        now = q.pop(0)
        for near in range(1, 101):
            if contact[now][near] and not visited[near]:
                visited[near] = visited[now] + 1
                q.append(near)

    max_node = 100
    for node in range(99, 0, -1):
        if visited[max_node] < visited[node]:
            max_node = node

    print(f'#{tc} {max_node}')
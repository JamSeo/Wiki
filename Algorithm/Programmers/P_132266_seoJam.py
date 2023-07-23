from collections import defaultdict, deque


def dijkstra(n, destination, adjN):
    adjM = [-1] * (n + 1)
    adjM[destination] = 0
    queue = deque([destination])
    visited = [0] * (n + 1)
    visited[destination] = 1

    while queue:
        now = queue.popleft()
        for near in adjN[now]:
            if not visited[near]:
                visited[near] = 1
                adjM[near] = adjM[now] + 1
                queue.append(near)

    return adjM


def solution(n, roads, sources, destination):
    # [1] 연결정보 저장
    adjN = defaultdict(list)
    for n1, n2 in roads:
        adjN[n1].append(n2)
        adjN[n2].append(n1)
    # [2] '도착지' 기준 각 노드까지의 거리 계산
    adjM = dijkstra(n, destination, adjN)
    answer = list(map(lambda x: adjM[x], sources))

    return answer


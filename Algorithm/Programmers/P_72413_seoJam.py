from heapq import heappop, heappush

def dijkstra(start):
    n = len(graph)
    adjM = [1e9 for _ in range(n)]
    adjM[start] = 0
    queue = [(0, start)]

    while queue:
        weight, now = heappop(queue)
        if adjM[now] < weight:
            continue
        for next, cost in graph[now]:
            ncost = cost + weight
            if ncost < adjM[next]:
                adjM[next] = ncost
                heappush(queue, (ncost, next))

    return adjM


def solution(n, s, a, b, fares):
    # [1] 인접정보 저장하기
    global graph
    graph = [[] for _ in range(n+1)]
    for n1, n2, cost in fares:
        graph[n1].append((n2, cost))
        graph[n2].append((n1, cost))

    # [2] Dijkstra 이용해서 최솟값 찾기
    answer = 1e9
    adjML = [[]] + [dijkstra(i) for i in range(1, n+1)]     # adjML: adjM 리스트
    for stop in range(1, n+1):                              # stop: A,B가 둘다 내리는 지점
        answer = min(answer, adjML[s][stop] + adjML[stop][a] + adjML[stop][b])

    return answer
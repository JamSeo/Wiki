# intensity 최소값의 gate-산봉우리 편도 경로만 고려해줌
import heapq
from collections import defaultdict

# 진짜 등산한거처럼 졸라 힘드네 4일동안 풀었다
def solution(n, paths, gates, summits):
    # [1] 경로 정보 저장
    # adjM = [[] for _ in range(n + 1)]
    adjM = defaultdict(list)
    for n1, n2, w in paths:
        adjM[n1].append((n2, w))
        adjM[n2].append((n1, w))

    # [2] dijkstra 알고리즘
    def dijkstra(max_weight=1e9):
        distance = [max_weight] * (n + 1)
        set_gates = set(gates)
        set_summits = set(summits)
        queue = []

        # 시작점 표시
        for gate in set_gates:
            distance[gate] = 0
            heapq.heappush(queue, (0, gate))  # [intensity, 현재노드]

        # 모든 정점 방문
        while queue:
            intensity, node = heapq.heappop(queue)
            # (1) 현재노드의 intensity 값이 distance 저장값보다 크거나, 현재노드가 산봉우리면? pass
            if distance[node] < intensity or node in set_summits:
                continue
            # (2) 그게 아니면? 현재노드와 이웃한 노드들의 distance 값 최신화
            for near, weight in adjM[node]:
                weight = max(distance[node], weight)
                if distance[near] > weight:
                    distance[near] = weight
                    heapq.heappush(queue, (weight, near))

        # [3] distance 최솟값을 갖는 산봉우리 노드 구하기
        answer = [0, max_weight]  # 최종 출력값
        summits.sort()
        for summit in summits:
            if distance[summit] < answer[1]:
                answer[0] = summit
                answer[1] = distance[summit]

        return answer

    return dijkstra()
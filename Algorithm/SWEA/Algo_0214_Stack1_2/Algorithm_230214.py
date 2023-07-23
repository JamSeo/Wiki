# DFS 예제
import sys
sys.stdin = open("sample_input.txt")
# V = vertice = 정점, E = Edge = rkstjs
# 갈 곳의 수, 길의 수
V, E = map(int, input().split())

# 인접정보 리스트
# index 0의 아이템 => [0에 인접한 점의 인덱스]
adjL = []
# 인접정보 2차원 리스트
# index 0의 아이템 => [1 if 인접 else 0 for i in range(V)]
adjM = [[0] * (V + 1) for _ in range(V + 1)]

# 인접정보
adj_data = list(map(int, input().split()))

# 인접정보 정리
for i in range(E):
    n1, n2 = adj_data[i * 2], adj_data[i * 2 + 1]
    adjM[n1][n2] = 1

# "점을 방문한 적 있는지"에 대한 정보
visited = [0 for _ in range(V + 1)]
# visited[i] == 1이면 i에 방문한 적 있음을 기록하는 리스트


# start는 시작점
def depth_first_search(start):
    stack = [start]

    # stack이 빌 때까지 반복
    while stack:
        now = stack.pop()
        # 미방문
        # 방문여부를 먼저 체크하고
        if visited[now] == 0:
            # 나 여기 왔어
            visited[now] = 1

            # next는 다음 점, V부터 1까지
            for next in range(V, 0, -1):
                # 연결되어 있고 아직 방문하지 않았으면
                if adjM[now][next] == 1 and visited[next] == 0:
                    # 방문할 곳에 기록한다
                    stack.append(next)


def depth_fist_search(ver):
    # 함수 호출 되면 거기 방문한것
    visited[ver] = 1
    # 작은수 부터 새기
    for next in range(1, V + 1):
        # 인접하고 미방문이면
        if adjM[ver][next] == 1 and visited[next] == 0:
            # 다음 함수 호출
            depth_first_search(next)

depth_first_search(1)
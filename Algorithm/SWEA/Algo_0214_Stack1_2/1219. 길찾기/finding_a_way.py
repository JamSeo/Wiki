import sys
sys.stdin = open("input.txt")

def depth_first_search(ver):
    # 99 도착하면 함수 종료
    if visited[99] == 1:
        return
    # 함수 호출 되면 거기 방문한것
    visited[ver] = 1
    # 작은수 부터 새기
    for next in range(1, 100):
        # 인접하고 미방문이면
        if adjM[ver][next] == 1 and visited[next] == 0:
            # 다음 함수 호출
            depth_first_search(next)


for _ in range(10):
    # 갈 곳의 수, 길의 수
    tc, E = map(int, input().split())
    # 인접정보 2차원 리스트
    # index 0의 아이템 => [1 if 인접 else 0 for i in range(V)]
    adjM = [[0] * (100) for _ in range(100)]
    # 순서쌍
    adj_data = list(map(int, input().split()))
    # 인접정보 정리
    for i in range(E):
        n1, n2 = adj_data[2*i], adj_data[2*i + 1]
        adjM[n1][n2] = 1

    # "점을 방문한 적 있는지"에 대한 정보
    # visited[i] == 1이면 i에 방문한 적 있음을 기록하는 리스트
    visited = [0 for _ in range(100)]

    depth_first_search(0)
    ans = 0
    if visited[99] == 1: ans = 1
    print(f'#{tc} {ans}')
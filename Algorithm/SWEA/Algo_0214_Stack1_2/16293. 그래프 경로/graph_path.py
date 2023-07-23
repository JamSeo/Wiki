import sys
sys.stdin = open("sample_input.txt")

def depth_first_search(ver):
    # 함수 호출 되면 거기 방문한것
    visited[ver] = 1
    # 작은수 부터 새기
    for next in range(1, V + 1):
        # 인접하고 미방문이면
        if adjM[ver][next] == 1 and visited[next] == 0:
            # 다음 함수 호출
            depth_first_search(next)


T = int(input())  # 테스트케이스

for tc in range(1, T + 1):
    # 갈 곳의 수, 길의 수
    V, E = map(int, input().split())

    # 인접정보 2차원 리스트
    # index 0의 아이템 => [1 if 인접 else 0 for i in range(V)]
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    # 인접정보 정리
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adjM[n1][n2] = 1

    # "점을 방문한 적 있는지"에 대한 정보
    # visited[i] == 1이면 i에 방문한 적 있음을 기록하는 리스트
    visited = [0 for _ in range(V + 1)]

    # 출발노드 S와 도착노드 G
    S, G = map(int, input().split())

    depth_first_search(S)
    ans = 0
    if visited[G] == 1: ans = 1
    print(f'#{tc} {ans}')
import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트케이스: 10

for tc in range(1, T+1):
    # N : int -- NxN 크기 배열 (5이상 15이하)
    # M : int -- MxM 크기 파리채 (2 이상 N 이하)
    # arr : 각 영역에 존재하는 파리의 개수 (30 이하)
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0
    for i in range(N-M+1):
        for j in range(N-M+1):

            flies = 0  # 파리채에 잡히는 파리의 수
            for di in range(M):
                for dj in range(M):
                    flies += arr[i+di][j+dj]

            if max_flies < flies:
                max_flies = flies

    print(f'#{tc} {max_flies}')



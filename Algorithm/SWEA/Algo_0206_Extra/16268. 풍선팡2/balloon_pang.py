import sys
sys.stdin = open("input1.txt")

T = int(input())  # 테스트케이스 : 1

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxM 크기의 격자판
    lst = [list(map(int, input().split())) for _ in range(N)]

    bal = []
    sum = 0

    for i in range(N):
        for j in range(M):

            if 0 < i < N-1 and 0 < j < M -1:
                sum = lst[i-1][j] + lst[i][j-1] + lst[i][j] + \
                       lst[i][j+1] + lst[i+1][j]

            elif i == 0:
                if j == 0:
                    sum = lst[i][j] + lst[i][j+1] + lst[i+1][j]
                elif j == M - 1:
                    sum = lst[i][j] + lst[i][j-1] + lst[i+1][j]
                else:
                    sum = lst[i][j] + lst[i][j-1] + lst[i][j+1] + lst[i+1][j]

            elif i == N-1:
                if j == 0:
                    sum = lst[i][j] + lst[i-1][j] + lst[i][j+1]
                elif j == M - 1:
                    sum = lst[i][j] + lst[i-1][j] + lst[i][j-1]
                else:
                    sum = lst[i][j] + lst[i][j-1] + lst[i][j+1] + lst[i-1][j]

            bal.append(sum)
            sum = 0

    res = 0
    for _ in range(N * M):
        if res < bal[_]:
            res = bal[_]

    print(f'#{tc} {res}')




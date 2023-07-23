import sys
sys.stdin = open("input.txt")

T = int(input())

# 시계방향 : 우 -> 하 -> 좌 -> 상
dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

for tc in range(1, T+1):
    print(f'#{tc}')

    # 0으로 된 NxN 격자 만들기
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # arr = [[0] * N] * N

    i, j = 0, 0
    k = 0  # 0:우, 1:하, 2:좌, 3:상

    for n in range(1, N**2 + 1):
        arr[i][j] = n
        new_j = j + dj[k]
        new_i = i + di[k]

        if (0 <= new_j < N) and (0 <= new_i < N) and (arr[new_i][new_j] == 0):
            j += dj[k]
            i += di[k]

        else:
            k = (k+1) % 4
            j += dj[k]
            i += di[k]

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()



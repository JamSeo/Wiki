import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 시계방향 : 우 -> 하 -> 좌 -> 상
dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

for tc in range(1, T+1):
    print(f'#{tc}')

    # 0으로 된 NxN 격자 만들기
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 리스트 받기
    lst= list(map(int, input().split()))
    lst.sort()

    i, j = 0, 0
    k = 0  # 0:우, 1:하, 2:좌, 3:상

    for n in range(N**2):
        arr[i][j] = lst[n]

        if (0<=(j+dj[k])<N) and (0<=(i+di[k])<N) and (arr[i+di[k]][j+dj[k]] == 0):
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



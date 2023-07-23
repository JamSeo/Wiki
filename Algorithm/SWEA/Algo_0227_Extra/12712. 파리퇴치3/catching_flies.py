import sys
sys.stdin = open("in1.txt")

dir1 = [(1, 0), (-1, 0), (0, -1), (0, 1)]
dir2 = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def catch1(arr, i, j):
    ans1 = arr[i][j]
    for mul in range(1, M):
        for k in range(4):
            ni, nj = i+mul*dir1[k][0], j+mul*dir1[k][1]
            if 0<=ni<N and 0<=nj<N:
                ans1 += arr[ni][nj]
    return ans1

def catch2(arr, i, j):
    ans2 = arr[i][j]
    for mul in range(1, M):
        for k in range(4):
            ni, nj = i + mul * dir2[k][0], j + mul * dir2[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                ans2 += arr[ni][nj]
    return ans2


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_ans = 0

    for i in range(N):
        for j in range(N):
            ans1 = catch1(arr, i, j)
            ans2 = catch2(arr, i, j)

            if max_ans < max(ans1, ans2):
                max_ans = max(ans1, ans2)

    print(f'#{tc+1} {max_ans}')
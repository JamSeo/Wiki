import sys
sys.stdin = open("input.txt")

# 12시부터 시계방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def DFS(tunnel, i, j):
    if tunnel[i][j] == 1:
        for k in range(4):
            new_i, new_j = i + di[k], j + dj[k]



T = int(input())

for tc in range(1, T + 1):
    N, M, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    # if tunnel[i][j] == 1:
    #     for k in range(4):
    #         new_i, new_j = i + di[k], j + djk]

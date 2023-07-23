import sys
sys.stdin = open("input.txt", "r")

# 전체를 순회! 미방문 -> 시작위치
# 내 값과 다음위치 값이 1차이가 난다면


def bfs(si, sj):
    q= []
    alst = []

    q.append((si,sj))
    v[si][sj] = 1
    alst.append(arr[si][sj])

    while q:
        ci,cj = q.pop(0)

        for di, dj in ((-1, 0), (1,0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and\
                abs(arr[ci][cj] - arr[ni][nj]) == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])

    return min(alst), len(alst)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v= [[0] * N for _ in range(N)]
    ans, cnt = N*N, 0
    for si in range(N):
        for sj in range(N):
            if v[si][sj] == 0:
                t, tcnt = bfs(si, sj)
                if cnt < tcnt or cnt == tcnt and ans > t:
                    ans, cnt = t, tcnt

    print(f'#{tc} {ans} {cnt}')
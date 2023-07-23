import sys
sys.stdin = open("sample_input.txt")

# 나 방향/ 범위내, 조건 -> q에 삽입
# 내가 이동항 방향 파이프에 내쪽 연결이 있으면
# 연결된 방향 P = [[],[0,1,2,3],[0,1],[2,3],[0,3,],[1,3],[1,2],[0,2]]
# opp={0:1, 1:0, 2:3, 3:2}
# for dir in P[arr[ci][cj]]  # 내 연결 방향
#   ni, nj 계산
#   if opp[dr] in P[arr[ni][nj]]: q삽입, v[n] <- v[c] + 1, cnt +1
# 종료조건:L 꺼냈는데 == L이면 v[ci][cj]

P = [[],[0,1,2,3],[0,1],[2,3],[0,3,],[1,3],[1,2],[0,2]]
opp = {0:1, 1:0, 2:3, 3:2}
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(si, sj ,L):
    q = []  # [0]
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return cnt

        for dr in P[arr[ci][cj]]:  # 현재위치 파이프에 연결된 방향
            ni, nj = ci + di[dr], cj + dj[dr]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 \
                and opp[dr] in P[arr[ni][nj]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    # 공간이 좁아서 L이전에 탐색이 끝난경우
    return cnt

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(R, C, L)
    print(f'#{tc} {ans}')
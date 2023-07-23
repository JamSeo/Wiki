import sys
input = sys.stdin.readline
from collections import deque

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):  # 국경 탐색 함수
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    united = [(i, j)]  # united: 같은 국경을 가진 국가 리스트

    while q:
        si, sj = q.popleft()
        # 4방향 탐색
        for dir in range(4):
            new_i, new_j = si+di[dir], sj+dj[dir]
            if new_i<0 or new_j<0 or new_i>=N or new_j>=N or visited[new_i][new_j]:
                continue
            if L <= abs(arr[si][sj] - arr[new_i][new_j]) <= R:  # 국경 여는지?
                visited[new_i][new_j] = 1                       # 국경 열면 방문처리
                q.append((new_i, new_j))
                united.append((new_i, new_j))
    return united


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = 0        # move: 인구이동 횟수
switch = True   # switch: 인구이동이 있으면 True, 없으면 False

while switch:
    visited = [[0]*N for _ in range(N)]
    switch = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                united = bfs(i, j)

                # 연합국의 수가 1보다 많으면 인구 이동
                if len(united) > 1:
                    switch = True
                    # new_population: 연합국의 새 인구
                    new_population = sum(arr[ui][uj] for ui, uj in united) // len(united)
                    for ui, uj in united:
                        arr[ui][uj] = new_population

    if switch == False:  # 인구 이동 없었으면? break
        break
    else:                # 인구 이동 있었으면? move +1
        move += 1

print(move)
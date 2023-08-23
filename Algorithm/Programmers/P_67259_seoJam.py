from collections import deque


def solution(board):
    N = len(board)
    MAX_VALUE = 1e7
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동서남북
    dp = [[[MAX_VALUE for _ in range(4)] for _ in range(N)] for _ in range(N)]

    dp[0][0] = [0] * 4  # 시작점
    queue = deque([(0, 0, 0), (0, 0, 2)])  # (row, column, dir)

    while queue:
        cr, cc, cdir = queue.popleft()

        for idx in range(4):
            nr, nc = cr + DIRS[idx][0], cc + DIRS[idx][1]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            if board[nr][nc]:
                continue

            new_value = dp[cr][cc][cdir] + (100 if cdir == idx else 600)

            if dp[nr][nc][idx] > new_value:
                dp[nr][nc][idx] = new_value
                queue.append((nr, nc, idx))

    return min(dp[-1][-1])

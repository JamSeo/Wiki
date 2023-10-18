# 참고 사이트: https://velog.io/@tjdud0123/%EB%B8%94%EB%A1%9D-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python
from collections import deque


def solution(board):
    N = len(board)
    TARGET = (N, N)

    queue = deque([((1, 1), (1, 2), 0)])  # (rob1, rob2, cnt)
    visited = set([((1, 1), (1, 2))])

    # board를 1로 패딩 => new_board
    # BFS 할 때 조건문 간단히 하기 위함.
    new_board = [[1 for _ in range(N + 2)] for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    while queue:
        rob1, rob2, cnt = queue.popleft()

        # 목표지점 도착하면?
        if rob1 == TARGET or rob2 == TARGET:
            return cnt

        # BFS
        for next_move in can_move(rob1, rob2, new_board):
            if next_move in visited:
                continue

            queue.append((*next_move, cnt + 1))
            visited.add(next_move)


def can_move(rob1, rob2, new_board):
    ROW, COL = 0, 1  # row, col
    DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = []

    # [1] 평행이동 탐색
    for dr, dc in DIRECTION:
        nrob1 = (rob1[ROW] + dr, rob1[COL] + dc)
        nrob2 = (rob2[ROW] + dr, rob2[COL] + dc)

        if (
            new_board[nrob1[ROW]][nrob1[COL]] == 0
            and new_board[nrob2[ROW]][nrob2[COL]] == 0
        ):
            res.append((nrob1, nrob2))

    # [2] 회전 탐색
    # [2-1] 로봇이 가로방향 일 때
    if rob1[ROW] == rob2[ROW]:
        UP, DOWN = -1, 1

        for dr in [UP, DOWN]:
            if (
                new_board[rob1[ROW] + dr][rob1[COL]] == 0
                and new_board[rob2[ROW] + dr][rob2[COL]] == 0
            ):
                if dr == UP:
                    res.append(((rob1[ROW] + dr, rob1[COL]), rob1))
                    res.append(((rob2[ROW] + dr, rob2[COL]), rob2))
                elif dr == DOWN:
                    res.append((rob1, (rob1[ROW] + dr, rob1[COL])))
                    res.append((rob2, (rob2[ROW] + dr, rob2[COL])))

    # [2-2] 로봇이 세로방향 일 때
    elif rob1[COL] == rob2[COL]:
        LEFT, RIGHT = -1, 1

        for dc in [LEFT, RIGHT]:
            if (
                new_board[rob1[ROW]][rob1[COL] + dc] == 0
                and new_board[rob2[ROW]][rob2[COL] + dc] == 0
            ):
                if dc == LEFT:
                    res.append(((rob1[ROW], rob1[COL] + dc), rob1))
                    res.append(((rob2[ROW], rob2[COL] + dc), rob2))
                elif dc == RIGHT:
                    res.append((rob1, (rob1[ROW], rob1[COL] + dc)))
                    res.append((rob2, (rob2[ROW], rob2[COL] + dc)))

    return res

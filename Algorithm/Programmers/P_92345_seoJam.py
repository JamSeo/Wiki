def solution(board, aloc, bloc):
    global n, m
    n, m = len(board), len(board[0])  # 행, 열
    _, answer = dfs(board, aloc, bloc)

    return answer


def is_in(r, c):
    if r < 0 or n <= r or c < 0 or m <= c:
        return False
    return True


def cant_move(board, loc):
    for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        nr, nc = loc[0]+dr, loc[1]+dc
        if is_in(nr, nc) and board[nr][nc]:
            return False
    return True


def dfs(board, nowPlayer, nextPlayer):
    # [1] 4방향에 갈 곳이 없으며? 짐
    if cant_move(board, nowPlayer):
        return [False, 0]

    # [2] 두 플레이어가 같은 위치에 있으면? 이김
    elif nowPlayer == nextPlayer:
        return [True, 1]

    r, c = nowPlayer
    can_win = False
    min_move = 1e9
    max_move = 0

    # [2] 4방향 탐색
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r+dr, c+dc

        if not is_in(nr, nc) or board[nr][nc] == 0:
            continue

        board[r][c] = 0
        result = dfs(board, nextPlayer, [nr, nc])  # 다음플레이어의 승리여부, 이동수
        board[r][c] = 1

        if not result[0]:
            can_win = True
            min_move = min(min_move, result[1])
        elif not can_win:
            max_move = max(max_move, result[1])

    move = min_move if can_win else max_move

    return [can_win, move + 1]
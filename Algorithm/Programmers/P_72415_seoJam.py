from copy import deepcopy
from collections import deque


def solution(board, r, c):
    global answer
    answer = 1e9
    pairs = list()

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                pairs.append((i, j))

    for nr, nc in pairs:
        dfs(r, c, nr, nc, pairs, board, 0)

    return answer


def dfs(r, c, nr, nc, pairs, board, cnt):
    global answer

    # 이미 answer 보다 많이 움직였다?
    if answer < cnt:
        return

    pairs = deepcopy(pairs)
    board = deepcopy(board)

    # [1] 첫 번째 짝카드로 이동
    cnt += distance(r, c, nr, nc, board)
    pairs.remove((nr, nc))

    # [2] 두 번째 짝 카드로 이동
    pr, pc = get_pair(nr, nc, pairs, board)
    cnt += distance(nr, nc, pr, pc, board)
    pairs.remove((pr, pc))

    board[nr][nc] = board[pr][pc] = 0  # 카드 뒤집기
    cnt += 2  # enter

    # [3] 더 맞출 짝이 없다면?
    if not pairs:
        answer = min(answer, cnt)
        return cnt

    # [4] 아직 맞춰야할 짝이 있다면?
    for tr, tc in pairs:
        dfs(pr, pc, tr, tc, pairs, board, cnt)


# (r, c)카드의 짝 카드 반환
def get_pair(r, c, pairs, board):
    for pair in pairs:
        pr, pc = pair
        if board[r][c] == board[pr][pc]:
            return pr, pc


# (r, c)에서 좌표별 최소이동횟수 반환
def distance(r, c, tr, tc, board):
    q = deque([])
    q.append((r, c))
    adjM = [[16 for _ in range(4)] for _ in range(4)]
    adjM[r][c] = 0  # 시작점 표시
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            r1, c1 = r + dr, c + dc
            r2, c2 = ctrl_move(r, c, dr, dc, board)

            if not is_in(r1, c1) or (r, c) == (r2, c2):
                continue
            # 최소 이동횟수 저장
            if adjM[r1][c1] > adjM[r][c] + 1:
                adjM[r1][c1] = adjM[r][c] + 1
                q.append((r1, c1))
            if adjM[r2][c2] > adjM[r][c] + 1:
                adjM[r2][c2] = adjM[r][c] + 1
                q.append((r2, c2))
            # 도착시 이동횟수 반환
            if (r1, c1) == (tr, tc):
                return adjM[r1][c1]
            if (r2, c2) == (tr, tc):
                return adjM[r2][c2]


# ctrl + 방향키
def ctrl_move(r, c, dr, dc, board):
    while is_in(r+dr, c+dc) and not board[r+dr][c+dc]:
        r, c = r + dr, c + dc
    if is_in(r+dr, c+dc) and board[r+dr][c+dc]:
        r, c = r + dr, c + dc
    return r, c


# board 안에 있는지 판단
def is_in(r, c):
    if r < 0 or 3 < r or c < 0 or 3 < c:
        return False
    return True


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
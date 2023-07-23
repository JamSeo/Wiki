# 지속된 시간초과로 인하여 구글링 좀 곁들였습니다.
import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ripe, ans = deque([]), 0

    # [1] 익은 감 위치 기억해두기
    for i in range(n):
        if 1 in box[i]:
            for j in range(m):
                if box[i][j] == 1:
                    ripe.append([i, j])
    # [2] BFS
    while ripe:
        i, j = ripe.popleft()
        for _ in range(4):
            ni, nj = i+dir[_][0], j+dir[_][1]
            if 0 <= ni < n and 0 <= nj < m and box[ni][nj] == 0:
                box[ni][nj] = box[i][j] + 1
                ripe.append([ni, nj])
    # [3] ans 구하기
    for lst in box:
        if 0 in lst:
            ans = -1
            break
        # 처음에 box[i][j] = 1로 시작했으니까 1 빼줌
        ans = max(ans, max(lst) - 1)

    print(ans)

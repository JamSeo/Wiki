# 끝내 구글링 했습니다.
import sys
input = sys.stdin.readline

def chess(color):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if not (i + j) % 2:
                value = board[i][j] != color  # if board[i][j] != color : value=1
            else:
                value = board[i][j] == color  # if board[i][j] == color : value=1
            prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] \
                                   - prefix_sum[i][j] + value

    count = sys.maxsize  # 64비트면 2**63 -1
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            count = min(count,
                        prefix_sum[i + K - 1][j + K - 1] - prefix_sum[i + K - 1][j - 1] \
                        - prefix_sum[i - 1][j + K - 1] + prefix_sum[i - 1][j - 1])
    return count


# N: 가로, M: 세로, K: 체스판
N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
print(min(chess('B'), chess('W')))
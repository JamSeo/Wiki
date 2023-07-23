import sys
sys.stdin = open("sample_input.txt")

# [1] 최초 대형 만들기
# [2] 해당 위치에 돌 놓아주고
# [3] 거기서 8방 검색 후 뻗어나가기
# [4] 다른 돌 발견하면 가운데 돌들 색 바꿔주기

def check(arr, i, j, color):
    # [2] 해당위치에 돌 놓기
    arr[i][j] = color
    # 8방향 : 12시부터 시계 방향
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    # [3] 거기서 8방 검색
    for k in range(8):  # 방향 탐색
        for mul in range(1, N):  # 거리 뻗어나가기
            new_i, new_j = i + mul * di[k], j + mul * dj[k]
            # 범위 설정
            if new_i < 0 or new_i >= N \
                    or new_j < 0 or new_j >= N \
                    or not arr[new_i][new_j]:
                break
            # 다른색 돌 발견하면 continue
            elif arr[new_i][new_j] != color:
                continue
            # [4] 같은색 돌 발견하면 가운데 돌들 색 바꿔주기
            else:
                for n in range(1, mul):
                    arr[i + n * di[k]][j + n * dj[k]] = color
                break


T = int(input())

for tc in range(1, T + 1):
    # N: 보드의 한 변의 길이, M: 돌을 놓는 횟수
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    # [1] 최초 대형
    m = N // 2
    board[m][m] = board[m-1][m-1] = 2
    board[m-1][m] = board[m][m-1] = 1

    for _ in range(M):
        # 돌이 놓일 좌표와 색
        si, sj, color = map(int, input().split())
        check(board, si - 1, sj - 1, color)

    # 흑돌, 백돌 개수 세주기
    black = white = 0
    for i in range(N):
        black += board[i].count(1)
        white += board[i].count(2)

    print(f'#{tc} {black} {white}')




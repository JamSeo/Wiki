import sys
sys.stdin = open("in.txt")

T = int(input())  # 테스트케이스: 3

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# # (dx, dy)  => arr[y+dy][x+dx]
# # left, right, up ,down
# directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

for tc in range(1, T+1):

    N = int(input())
    # arr = []
    # for _ in range(N):
    #     arr.append(list(map(int, sys.stdin.readline().split())))
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # N*N 2차원 배열 받기

    total_sum = 0

    for i in range(N):  # i는 y
        for j in range(N):  # j는 x
            # print(f'i: {i}, j: {j}, arr[i][j]: {arr[i][j]}')
            this_sum = 0

            for dir in range(4):
                cmp_x = j + dx[dir]
                cmp_y = i + dy[dir]

                if 0<= cmp_x <5 and 0<= cmp_y <5:  # idx가 범위안에 들어오는지 확인
                    this_sum = arr[i][j] - arr[cmp_y][cmp_x]

                    if this_sum >= 0:  # 절댓값 더해주기
                        total_sum += arr[i][j] - arr[cmp_y][cmp_x]
                    else:
                        total_sum += -this_sum

    print(f"#{tc} {total_sum}")
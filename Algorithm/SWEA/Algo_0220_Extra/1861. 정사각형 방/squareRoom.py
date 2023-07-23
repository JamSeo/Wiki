import sys
sys.stdin = open("input.txt")

# 12시부터 시계방향
di = [-1, 0, 1, 0]
dj = [0, -1 ,0 ,1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 1

    for i in range(N):
        for j in range(N):
            cnt = 1
            stack = [(i, j)]
            while stack:
                si , sj = stack.pop()
                for k in range(4):
                    new_i, new_j = si + di[k], sj + dj[k]
                    if 0 <= new_i < N and 0 <= new_j < N  \
                            and room[new_i][new_j] == room[si][sj] + 1:
                            cnt += 1
                            stack.append((new_i, new_j))
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                    res = room[i][j]
                elif max_cnt == cnt:
                    res = min(res, room[i][j])

    print(f'#{tc} {res} {max_cnt}')
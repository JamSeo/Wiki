if __name__ == '__main__':

    # N:격자크기  M:볼 개수  K:이동횟수
    N, M, K = map(int, input().split())

    # fballs: 파이어볼 리스트
    fballs = []
    for _ in range(M):
        # r:행  c:열  m:질량  s:속도  d:방향
        r, c, m, s, d = map(int, input().split())
        fballs.append([r-1, c-1, m, s, d])

    # arr: NxN 격자, dir: 방향 리스트
    arr = list([[] for _ in range(N)] for _ in range(N))
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for _ in range(K):
        # 파이어볼 이동
        while fballs:
            cr, cc, cm, cs, cd = fballs.pop()
            new_r = (cr + cs * dir[cd][0]) % N      # 행 이동
            new_c = (cc + cs * dir[cd][1]) % N      # 열 이동
            arr[new_r][new_c].append([cm, cs, cd])  # 좌표입력

        # 같은 칸에 두 개 이상의 파이어볼이 있는지 검색
        for i in range(N):
            for j in range(N):
                if len(arr[i][j]) == 1:         # 1개 있으면?
                    fballs.append([i, j] + arr[i][j].pop())

                elif len(arr[i][j]) > 1:        # 2개 이상이면?
                    sum_m, sum_s, len_ball = 0, 0, len(arr[i][j])
                    num = arr[i][j][0][2] % 2
                    new_dir = "even"

                    while arr[i][j]:
                        ball = arr[i][j].pop()
                        sum_m += ball[0]
                        sum_s += ball[1]
                        if ball[2] % 2 != num:  # 하나라도 홀수/짝수 통일이 안되면?
                            new_dir = "odd"     # 새 방향은 홀수방향

                    if not sum_m//5:   # 질량이 없으면 넘어가.
                        continue
                    else:
                        for k in range(4):
                            if new_dir == "even":
                                fballs.append([i, j, sum_m//5, sum_s//len_ball, k*2])
                            else:
                                fballs.append([i, j, sum_m//5, sum_s//len_ball, k*2+1])

    print(sum(fball[2] for fball in fballs))







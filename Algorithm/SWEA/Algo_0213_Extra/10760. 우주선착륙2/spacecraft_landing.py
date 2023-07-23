import sys
sys.stdin = open("input2.txt")

# check 착륙지점을 기준으로 8개 방향 확인(12시부터 시계방향 순)
# if 착륙지점보다 숫자가 작으면 cnt +1
#   if cnt == 4가 되면 result +1 후 break
# else cnt < 4면 break
# break 되면 다음 착륙지 검색

# check(): 주변 검색하는 함수
def check(arr, N, M, i, j):
    global res

    # 12시부터 시계방향 순
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    cnt = 0
    for k in range(8):  # 새좌표 설정
        new_i = i + di[k]
        new_j = j + dj[k]

        if new_i < 0 or new_i >= N or \
                new_j < 0 or new_j >= M:        # 새좌표가 리스트 밖이다?
            continue
        elif arr[i][j] <= arr[new_i][new_j]:    # 새좌표가 착륙지 보다 더 높다?
            continue
        else:                                   # 착륙지보다 낮으면 cnt +1
            cnt += 1
            if cnt == 4:                        # cnt ==4가 되면 res +1 후 return
                res += 1
                return
    else:                                       # 탐색이 끝나도 cnt < 4이면 return
        if cnt < 4: return


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    district = [list(map(int, input().split())) for _ in range(N)]

    res = 0

    for i in range(N):
        for j in range(M):
            check(district, N, M, i, j)

    print(f'#{tc} {res}')

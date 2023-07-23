import sys
sys.stdin = open("sample_input.txt")

# [1] 초기 모양 배치
# [2] arr[si][sj] = d
# - 8방향 뻗어나가면서
# arr[ni][nj]
# O : break
# 다른돌 : 후보(좌표) / temp_lst에 추가
# 같은돌 : temp_lst 뒤집기

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # arr 네 방향 0으로 패딩해서 둘러쌈
    arr = [[0] * (N+2) for _ in range(N + 2)]
    m = N // 2
    # [1] 초기 모양 배치
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m+1][m] = arr[m][m+1] = 1

    # [2] 흑돌, 백돌 받아서 입력 처리
    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 처리
        for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            # 해당방향으로 뻗어 나가면서 처리
            temp_lst = []
            for mul in range(1, N):
                ni, nj = si+di*mul, sj+dj*mul
                if arr[ni][nj] == 0:    # 빈칸 범위 밖
                    break
                elif arr[ni][nj] != d:  # 다른 돌인 경우
                    temp_lst.append((ni, nj))
                else:                   # 같은돌 => 후보들을 뒤집고, 종료
                    while temp_lst:
                        ti, tj = temp_lst.pop()
                        arr[ti][tj] = d
                    break
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')
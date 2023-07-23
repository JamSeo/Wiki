for tc in range(1, 11):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 열(j): 0 -> N 순서로 해당 행(i) 검색
    for j in range(N):
        # 행(i): 0 -> N 순서로 검색
        i = 0
        while i < N:
            if square[i][j] == 1:           # 1을 발견하면?
                for k in range(i + 1, N):   # 1 아래에 2가 있는지 검색
                    if square[k][j] == 2:   # 2가 나오면?(== 교착 O)
                        ans += 1                # 교착상태 +1
                        i = k                   # 2 아래부터 다시 검색
                        break
                else:                       # 2가 안나오면?(== 교착 X)
                    break                       # 다음 열(j)검사하기
            i += 1

    print(f'#{tc} {ans}')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []  # 결과값 도출용 리스트

    for i in range(N):
        for j in range(N):
            # [1] 0이 아닌 숫자 만나면 길이 측정
            if arr[i][j]:
                ni, nj = i, j
                width = length = 0
                while arr[ni][j] and ni < N:  # 세로길이 측정
                    length += 1
                    ni += 1
                while arr[i][nj] and nj < N:  # 가로길이 측정
                    width += 1
                    nj += 1
                ans.append([length, width])   # ans에 저장

                # [2] 측정이 끝나면 숫자칸을 0으로 바꿔줌
                for k in range(i, ni):
                    for l in range(j, nj):
                        arr[k][l] = 0

    # [3] 행과 열을 곱한 값 기준으로 정렬 (단, 같으면 세로길이 기준)
    ans.sort(key = lambda x: (x[0] * x[1], x[0]))
    len_ans = len(ans)
    ans = sum(ans, [])
    print(f'#{tc}', len_ans, *ans)
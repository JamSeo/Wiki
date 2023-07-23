def solution(board, skill):
    # [0] pre_sum 2차원 리스트 만들기
    n = len(board)
    m = len(board[0])
    pre_sum = list([0]*(m+1) for _ in range(n+1))

    # [1] 각 모서리 점 찍기
    for type_, r1, c1, r2, c2, degree in skill:
        sign = -1 if type_ == 1 else 1
        pre_sum[r1][c1] += sign * degree
        pre_sum[r1][c2+1] -= sign * degree
        pre_sum[r2+1][c1] -= sign * degree
        pre_sum[r2+1][c2+1] += sign * degree

    # [2] 가로 누적합
    for i in range(n+1):
        sum_ = 0
        for j in range(m+1):
            sum_ += pre_sum[i][j]
            pre_sum[i][j] = sum_

    # [3] 세로 누적합
    for j in range(m+1):
        sum_ = 0
        for i in range(n+1):
            sum_ += pre_sum[i][j]
            pre_sum[i][j] = sum_

    # [4] 건물 훑기
    answer = 0
    for i in range(n):
        for j in range(m):
            if pre_sum[i][j] + board[i][j] > 0:
                answer += 1

    return answer
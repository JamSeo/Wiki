def solution(m, n, puddles):
    arr = [[0] * (m+1) for _ in range(n+1)]
    arr[1][1] = 1  # 출발점 표시
    # 탐색하면서 칸 별로 도달 가능한 경우의 수 저장
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                continue
            arr[i][j] += arr[i-1][j] + arr[i][j-1]

    answer = arr[n][m] % 1000000007
    return answer
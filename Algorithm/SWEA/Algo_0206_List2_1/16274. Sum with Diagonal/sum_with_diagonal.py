import sys
sys.stdin = open("sum_input.txt")

for _ in range(10):
    tc = int(input())

    arr = []  # arr : 주어진 100X100의 2차원 배열
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 각 행의 합 중 최댓값
    result = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]

        if result < sum:
            result = sum

    # 각 열의 합 중 최댓값
    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]

        if result < sum:
            result = sum

    # 대각선의 합 중 최댓값
    for i in range(100):
        j = i
        sum = arr[i][j]

        if result < sum:
            result = sum

    for i in range(100):
        j = -1 - i
        sum = arr[i][j]

        if result < sum:
            result = sum

    print('#{} {}'.format(tc, result))

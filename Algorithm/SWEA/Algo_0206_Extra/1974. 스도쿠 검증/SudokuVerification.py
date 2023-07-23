import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    a1 = lst  # 가로
    a2 = [list(lst[i][j] for i in range(9)) for j in range(9)]  # 세로
    a3 = []  # 3x3 격자
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            a3.append(lst[i][j:j+3] + lst[i+1][j:j+3] + lst[i+2][j:j+3])

    ans = 1
    for i in range(9):
        if len(set(a1[i])) != 9:
            ans = 0

        elif len(set(a2[i])) != 9:
            ans = 0

        elif len(set(a3[i])) != 9:
            ans = 0

    print(f'#{tc} {ans}')
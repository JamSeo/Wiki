import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    K, ans = N // 2, 0

    for i in range(N):
        for j in range(N):
            if abs(i - K) + abs(j - K) <= K:
                ans += farm[i][j]

    print(f'#{tc} {ans}')
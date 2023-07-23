T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    ans = 0

    score.sort(reverse=True)
    for i in range(K):
        ans += score[i]
    print(f'#{tc} {ans}')
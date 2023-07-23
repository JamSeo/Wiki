T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bill = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * 8

    for i in range(8):
        ans[i] += N // bill[i]
        N %= bill[i]

    print(f'#{tc}')
    print(*ans)
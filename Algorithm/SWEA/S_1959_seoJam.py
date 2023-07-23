T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_ = 0

    if M < N:
        A, B = B, A
        N, M = M, N

    for n in range(M - N + 1):
        sum_ = 0
        for idx in range(N):
            sum_ += A[idx] * B[idx + n]

        if max_ < sum_:
            max_ = sum_

    print(f'#{tc} {max_}')
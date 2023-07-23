def solution(sequence):
    n = len(sequence)
    pulse1 = list(sequence[idx] if idx % 2 else -sequence[idx] for idx in range(n))  # (-1, 1) 순으로 곱해준 수열
    pulse2 = list(map(lambda x: -x, pulse1))                                         # (1, -1) 순으로 곱해준 수열
    dp1 = [pulse1[0]] + [0] * (n - 1)  # pulse1에서 부분 수열의 합
    dp2 = [pulse2[0]] + [0] * (n - 1)  # pulse2에서 부분 수열의 합

    # [1] 비교: 현재 idx 수열값  vs  현재 idx 까지의 연속된 수열의 합
    for i in range(1, n):
        dp1[i] = max(pulse1[i], dp1[i-1] + pulse1[i])
        dp2[i] = max(pulse2[i], dp2[i-1] + pulse2[i])

    # [2] dp1과 dp2의 최댓값 중 더 큰값 반환
    return max(max(dp1), max(dp2))


# print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
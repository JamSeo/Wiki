import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트케이스: 3
A = [num for num in range(1, 13)]  # 집합 A : 1부터 12까지의 숫자를 원소로 가진 집합

for tc in range(1, T+1):
    # N : int -- 부분집합 원소의 수 (1 ≤ N ≤ 12)
    # K : int -- 부분집합의 합  (1 ≤ K ≤ 100)
    N, K = map(int, input().split())
    cnt = 0  # 문제조건에 해당하는 부분집합의 수

    for i in range(1, 1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):

                subset.append(A[j])  # 부분집합 완성!~!~!

        if len(subset) == N and sum(subset) == K:  # 문제조건
            cnt += 1

    print(f'#{tc} {cnt}')

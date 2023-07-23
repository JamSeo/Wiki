from itertools import combinations
import sys
sys.stdin = open("in2.txt")

T = int(input())  # 테스트케이스: 3

for tc in range(1, T+1):

    arr = list(map(int, input().split()))  # 10개 숫자 입력 받기
    N = len(arr)

    for i in range(1, 1 << N):  # 1부터 2ⁿ 까지 반복
        subset_sum = 0

        for j in range(N):
            if i & (1 << j):
                subset_sum += arr[j]  # 부분집합의 elem : arr[j]

        if subset_sum == 0:
            print(f'#{tc} 1')
            break

    else:
        print(f'#{tc} 0')

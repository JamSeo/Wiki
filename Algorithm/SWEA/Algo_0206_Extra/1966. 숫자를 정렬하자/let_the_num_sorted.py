import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트케이스: 10

for tc in range(1, T + 1):
    N = int(input())  # 숫자열 길이
    nums = list(map(int, input().split()))
    i = 0

    while i < N:
        min_num = nums[i]
        for j in range(i + 1, N):
            if nums[j] < min_num:
                min_num = nums[j]
        for k in range(i + 1, N):
            if nums[k] == min_num:
               nums[i], nums[k] = nums[k], nums[i]
        i += 1

    print(f'#{tc}', *nums)







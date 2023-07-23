import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테이스 케이스 수  # 1 ≤ T ≤ 50

for i in range(1, T+1):
    N = int(input())  # 5 ≤ N ≤ 1000
    a = list(map(int, input().split()))  # 1 ≤ a ≤ 1000000

    min_a = a[0]  # 리스트 최소값
    for num in a:
        if min_a >= num:
            min_a = num

    max_a = a[0]  # 리스트 최대값
    for num in a:
        if max_a <= num:
            max_a = num

    result = max_a - min_a  # 결과값 = 최대값 - 최소값

    print("#{} {}".format(i, result))
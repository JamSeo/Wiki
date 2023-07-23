import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 수

for i in range(1, T+1):
    N, M = tuple(map(int, input().split()))  # N, M 입력  # 10 ≤ N ≤ 100,  2 ≤ M ＜ N
    a = list(map(int, input().split()))   # 1 ≤ a ≤ 10000

    lst_sum = list()  # 합계값 저장 리스트

    for j in range(N-M+1):
        a_sum = 0
        for n in range(M):
            a_sum += a[j+n]   # 이웃한 숫자 M개 합계

        lst_sum.append(a_sum)  # 리스트에 합계값 저장

    min_lst = lst_sum[0]  # 리스트 최소값 구하기
    for num in lst_sum:
        if num <= min_lst:
            min_lst = num

    max_lst = lst_sum[0]  # 리스트 최대값 구하기
    for num in lst_sum:
        if num >= max_lst:
            max_lst = num

    result = max_lst - min_lst  # 최대값과 최소값 차

    print("#{} {}".format(i, result))


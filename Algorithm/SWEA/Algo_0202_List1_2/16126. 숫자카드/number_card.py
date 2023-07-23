import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트케이스 수

for tc in range(1, T+1):
    N = int(input())  # 카드 장수

    a = input()  # 49679
    A = list(a)  # ['4', '9', '6', '7', '9']
    A = list(map(int, A))  # [4, 9, 6, 7, 9]
    max_A = max(A)  # 9
    c = [0] * (max_A + 1)  # [0] * 10

    for i in range(N):  # N == len(A) ; 5
        c[A[i]] += 1  # c = [0,0,0,0,1,0,1,1,0,2]

    max_num = c[0]  # c에서 가장 큰 값 ; 가장 많은 카드 갯수
    max_idx = 0  # c에서 가장 큰 값의 idx ; 가장 많은 카드의 숫자
    for idx in range(len(c)):  # range(10)
        if max_num <= c[idx]:
            max_num = c[idx]
            max_idx = idx


    print("#{} {} {}".format(tc, max_idx, max_num))
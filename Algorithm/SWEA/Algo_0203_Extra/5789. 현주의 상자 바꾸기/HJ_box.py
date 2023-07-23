import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스: 1

for tc in range(1, T+1):
    N, Q = map(int, input().split())  # N(상자개수): 5, Q(작업수): 2

    box = [0] * N  # N개의 0이 적힌 박스 []

    for i in range(1, Q+1):
        L, R = map(int, input().split())  # L: 1, R: 3 ==> idx: 0 ~ 2

        box[L-1:R] = [i] * (R-L+1)  # L부터 R까지 슬라이싱 후 i 넣기

    print(f"#{tc}", *box)




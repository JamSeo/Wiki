import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트케이스: 2

for tc in range(1, T+1):
    A, B = input().split()

    a = len(A)
    b = len(B)

    cnt = A.count(B)

    ans = a - cnt * (b - 1)

    print(f'#{tc} {ans}')





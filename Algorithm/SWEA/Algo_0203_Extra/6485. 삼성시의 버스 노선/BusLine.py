import sys
sys.stdin = open("s_input.txt")

T = int(input())  # 테스트케이스 : 1

for tc in range(1, T+1):
    N = int(input())  # 버스노선 수; N번 반복하면서 노선입력, 빈도수 표시

    cnts = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())

        for i in range(A, B+1):
            cnts[i] += 1

    P = int(input())
    lst= []
    for _ in range(P):
        p = int(input())
        lst.append(cnts[p])

    print(f'#{tc}', *lst)
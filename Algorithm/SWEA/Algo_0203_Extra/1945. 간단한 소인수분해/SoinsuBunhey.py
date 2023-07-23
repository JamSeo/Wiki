import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스 : 10

for tc in range(1, T+1):

    N = int(input())
    lst = [0] * 5  # a,b,c,d,e 저장[]

    while N != 1:

        if N % 2 == 0:
            N //= 2
            lst[0] += 1
            continue

        if N % 3 == 0:
            N //= 3
            lst[1] += 1
            continue

        if N % 5 == 0:
            N //= 5
            lst[2] += 1
            continue

        if N % 7 == 0:
            N //= 7
            lst[3] += 1
            continue

        if N % 11 == 0:
            N //= 11
            lst[4] += 1
            continue

    print(f"#{tc}", *lst)
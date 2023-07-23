import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))

    cnt = 1
    lst = [1]

    for i in range(1, N):
        if (C[i-1] + 1) == C[i]:
            cnt += 1
            lst.append(cnt)
        else:
            cnt = 1
    max_lst = max(lst)

    print("#{} {}".format(tc, max_lst))
import sys
sys.stdin = open("test_input.txt", 'rt', encoding='UTF8')

for _ in range(10):
    tc = int(input())
    p = input()
    t = input()

    M = len(p)
    N = len(t)

    cnt = 0

    for i in range(N - M + 1):
        if p == t[i : i + M]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
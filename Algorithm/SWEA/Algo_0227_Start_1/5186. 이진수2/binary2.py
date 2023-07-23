import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    ans = ''
    cnt = 0

    while N:
        ans += str(int(N * 2))
        N = N * 2 - int(N * 2)
        cnt += 1
        if cnt == 13:
            print('overflow')
            break
    else:
        print(ans)
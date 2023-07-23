import sys
sys.stdin = open("sample_input.txt")

def paste_paper(N):
    n = N // 10
    if n == 1: return 1
    elif n == 2: return 3
    else:
        return paste_paper(N - 10) + 2 * paste_paper(N - 20)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    res = paste_paper(N)
    print(f'#{tc} {res}')
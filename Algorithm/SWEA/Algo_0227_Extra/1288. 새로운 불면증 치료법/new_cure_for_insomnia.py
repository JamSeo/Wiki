import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    arr = []

    while len(arr) != 10:
        ans += 1
        N *= ans
        lst_N = list(str(N))

        for i in lst_N:
            if i not in arr:
                arr.append(i)
        N //= ans

    print(f'#{tc} {ans * N}')
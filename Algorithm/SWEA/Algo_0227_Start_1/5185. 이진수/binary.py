import sys
sys.stdin = open("sample_input.txt")

def ten_to_binary(n):
    ans = ''
    for _ in range(4):
        ans = str(n % 2) + ans
        n //= 2
    return ans


T = int(input())
alp_to_num = [['A', 10], ['B', 11], ['C', 12], ['D', 13], ['E', 14], ['F', 15]]

for tc in range(1, T + 1):
    N, num16 = input().split()
    N = int(N)
    num16 = list(num16)
    ans = ''

    for i in range(N):
        if num16[i].isdecimal():
            num16[i] = int(num16[i])
        else:
            for alp in alp_to_num:
                if num16[i] == alp[0]:
                    num16[i] = alp[1]
                    break

    res = ''
    for i in num16:
        res += ten_to_binary(i)

    print(f'#{tc} {res}')
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x = round(N**(1/3))

    if x**3 == N:
        print(f'{tc} {x}')
    else:
        print(f'{tc} -1')

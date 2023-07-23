import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = [0] * N

    for _ in range(M % N):
        for i in range(N):
            temp[i-1] = arr[i]
        arr = temp

    print(f'#{tc} {arr[0]}')

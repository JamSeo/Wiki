import sys
sys.stdin = open("input1.txt")

def dig(arr):
    max_len = 2
    for lst in arr:
        length = 0
        for remains in lst:
            if remains:
                length += 1
                if max_len < length:
                    max_len = length
            else: length = 0
    return max_len


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 사진의 해상도 NxM
    data = [list(map(int, input().split())) for _ in range(N)]  # 사진 데이터
    data_t = list(map(list, zip(*data)))

    ans = max(dig(data), dig(data_t))

    print(f'#{tc} {ans}')



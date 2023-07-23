import sys
sys.stdin = open("input1.txt")

def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
                if mx < cnt:
                    mx = cnt
            else:
                cnt = 0
    return mx


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 사진의 해상도 NxM
    arr = [list(map(int, input().split())) for _ in range(N)]  # 사진 데이터
    arr_t = list(map(list, zip(*arr)))  # [[0, 0, 0], [1, 1, 1], [0, 0, 0]]

    ans = count(arr)
    t = count(arr_t)
    if ans < t:
        ans = t

    print(f'#{tc} {ans}')
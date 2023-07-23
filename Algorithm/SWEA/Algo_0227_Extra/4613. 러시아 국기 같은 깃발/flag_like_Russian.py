import sys
sys.stdin = open("sample_input.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_cnt = 2500
    temp = []

    for i in range(1, N-1):         # i: 'W'가 칠해질 줄 수
        for j in range(1, N-i):     # j: 'B'가 칠해질 줄 수
            k = N - i - j           # k: 'R'가 칠해질 줄 수
            cnt = 0
            temp = []               # temp: 각 경우의 수 저장

            for n in range(i):
                temp.append('W')
            for n in range(j):
                temp.append('B')
            for n in range(k):
                temp.append('R')

            for idx, col in enumerate(temp):
                for flag in arr[idx]:
                    if flag != col:
                        cnt += 1

            if cnt < min_cnt:
                min_cnt = cnt

    print(f'#{tc+1} {min_cnt}')


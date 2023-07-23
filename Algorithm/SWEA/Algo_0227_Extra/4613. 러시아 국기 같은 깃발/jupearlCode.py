import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    area = [input() for _ in range(N)]

    count_color = [[] for _ in range(N)]
    for i in range(N):
        A = area[i].count('W')
        B = area[i].count('B')
        count_color[i].extend([A, B, M - A - B])

    min_fi = N * M
    for i in range(1, N - 1):           # i가 'B'가 시작되는 줄
        for j in range(i + 1, N):       # j가 'R'가 시작되는 줄
            temp = 0
            for k in range(N):          # k가 0부터 N-1까지 긁으면서 바꿔칠해야하는 깃발 수 세어줌
                if k < i:
                    temp += M - count_color[k][0]
                elif i <= k < j:
                    temp += M - count_color[k][1]
                elif j <= k:
                    temp += M - count_color[k][2]
                if temp >= min_fi:      # back_tracking, 만약 최솟값보다 크면 break
                    break
            if temp < min_fi:
                min_fi = temp

    print(f'#{tc} {min_fi}')
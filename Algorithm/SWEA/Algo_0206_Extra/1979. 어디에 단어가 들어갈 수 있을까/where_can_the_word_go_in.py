import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N: int -- 단어 퍼즐의 가로세로 길이
    # K: int -- 단어의 길이
    # puz: 1차원 [] -- 단어 퍼즐의 모양
    N, K = map(int, input().split())
    puz = [list(map(int, input().split())) for _ in range(N)]

    # res: int -- 길이 K인 단어가 들어갈 수 있는 자리의 수
    res = 0

    # 가로 방향 검사
    for i in range(N):
        cnt = 0
        for j in range(N):

            # 값이 1 이면, cnt +1
            if puz[i][j]:
                cnt += 1

            # 값이 0이거나, 인덱스가 N-1에 도착하면, cnt와 K가 같은지 확인 후 res +1
            if (not puz[i][j]) or (j == N - 1):
                if cnt == K:
                    res += 1
                    print(i,j)
                # cnt 초기화
                cnt = 0

    # 세로 방향 검사 : 이하 동문
    for j in range(N):
        cnt = 0
        for i in range(N):
            if puz[i][j]:
                cnt += 1
            if (not puz[i][j]) or (i == N - 1):
                if cnt == K:
                    res += 1
                cnt = 0

    print(f'#{tc} {res}')
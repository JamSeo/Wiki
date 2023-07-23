import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N : 오목판 크기(5 ≤ N ≤ 20)
    omok = [input() for _ in range(N)]  # 오목판 문자열 받기
    num = 0  # num : int -- 5개 연속한 부분의 개수

    # 가로방향 검사
    for i in range(N):
        if 'ooooo' in omok[i]:
            num += 1

    # 세로방향 검사 :
    for i in range(N-4):
        for j in range(N):
            for move in range(5):
                if omok[i + move][j] != 'o':
                    break
            else:
                num += 1

    # 대각방향 검사 :
    for i in range(N-4):
        for j in range(N-4):
            for move in range(5):
                if omok[i + move][j + move] != 'o':
                    break
            else:
                num += 1

    # 역대각방향 검사:
    for i in range(N-4):
        for j in range(N-1, 3, -1):
            for move in range(5):
                if omok[i + move][j - move] != 'o':
                    break
            else:
                num += 1

    if num >= 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')



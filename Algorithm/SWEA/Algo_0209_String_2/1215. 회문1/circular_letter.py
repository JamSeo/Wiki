import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    K = int(input())  # K: 회문의 길이
    words = [input() for _ in range(8)]  # words: 8x8 크기의 글자판 []

    res = 0
    # 가로방향 검사
    for i in range(8):
        for j in range(9 - K):
            if words[i][j:j+K] == words[i][j:j+K][::-1]:
                res += 1

    # 세로방향 검사
    for j in range(8):
        for i in range(9-K):
            word = ''
            for k in range(K):
                word += words[i+k][j]

            if word == word[::-1]:
                res += 1

    print(f'#{tc} {res}')
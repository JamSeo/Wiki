import sys
sys.stdin = open("input.txt")

def is_palindrome(word):
    return word == word[::-1]

def solve(word, max_size):
    # 현재 100자 중 K 글자짜리 회문이 있는지 검사
    for K in range(100, 0, -1):  # K : 단어 길이
        # 만약 K가 내가 아는 최대보다 작거나 같은면 for문 탈출
        if K < max_size:
            break
        for idx in range(100 - K + 1):
            # 회문인지 검사
            if is_palindrome(word[idx:idx+K]):
                return K
    return max_size


for tc in range(1, 11):
    input()

    words = list(input() for _ in range(100))
    words_ver = []  # ver(;vertical)
    for i in range(100):
        tmp = ''
        for j in range(100):
            tmp += words[j][i]
        words_ver.append(tmp)

    res = 0
    # 가로 검사
    for word in words:
        res = solve(word, res)
    # 세로 검사
    for word in words_ver:
        res = solve(word, res)

    print(f'#{tc} {res}')

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    lst = [input() for _ in range(5)]
    # M: [] -- 입력된 문자열 중 가장 긴 문자열 길이
    # res: str -- 세로로 읽은 순서의 문자열
    M = max(len(lst[i]) for i in range(5))
    res = ''

    # 문자열 길이가 M보다 작으면 M보다 작은 만큼 '#'을 추가
    for i in range(5):
        if len(lst[i]) < M:
            while len(lst[i]) < M:
                lst[i] += '#'

    # 문자열을 세로로 읽은 순서대로 저장하는데,
    # 이때 '#'이 나오면 저장 X
    for j in range(M):
        for i in range(5):
            if '#' == lst[i][j]:
                continue
            res += lst[i][j]

    print(f'#{tc} {res}')
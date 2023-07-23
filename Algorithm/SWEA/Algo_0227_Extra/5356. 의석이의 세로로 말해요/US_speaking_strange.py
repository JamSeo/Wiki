import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    ans = ''
    max_len = 0

    # 문자열 최대 가로길이 구하기
    for lst in arr:
        if max_len < len(lst):
            max_len = len(lst)
    # 문자열 길이가 최대길이 보다 짧으면 짦은만큼 '_' 추가하기
    for lst in arr:
        if max_len > len(lst):
            for _ in range(len(lst), max_len):
                lst.append('_')
    # '_' 빼고 답안 출력하기
    for j in range(max_len):
        for i in range(5):
            if arr[i][j] == '_':
                pass
            else: ans += arr[i][j]
    print(f'#{tc}', ans)


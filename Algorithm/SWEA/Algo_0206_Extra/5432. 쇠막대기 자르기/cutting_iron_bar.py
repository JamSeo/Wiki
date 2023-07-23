import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    bar = input()
    N = len(bar)
    cnt = []  # cnt: [] -- 막대가 잘리는 횟수 리스트
    cut = stick = 0  # cut: 막대가 잘리는 횟수, stick: 원래 막대기 수

    # for문 범위 : 입력된 문자열 bar의 길이
    #
    for i in range(N):
        if bar[i] == '(' and bar[i + 1] == ')':
            cnt.append(cut)
        elif bar[i] == ')' and bar[i - 1] == '(':
            continue
        elif bar[i] == '(':
            cut += 1
            stick += 1
        else:
            cut -= 1
    # 결과값 출력
    ans = sum(cnt) + stick
    print(f'#{tc} {ans}')
import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트케이스 : 10

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    text = []

    for _ in range(N):
        alp, num = input().split()
        num = int(num)
        text.append(alp * num)
    text = "".join(text)

    M = len(text)

    for idx in range(M):
        if idx == M - 1 or idx % 10 == 9:
            print(text[idx])
        else:
            print(text[idx], end='')






import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    # 문자열 계산식 길이
    N = int(input())
    # 받아올 수식 문자열
    expression = input()
    stack = []
    # 출력 문자열
    result = ''

    for token in expression:
        # 숫자면 result에 추가
        if token.isdecimal():
            result += token
        # '+'이면 stack에 추가
        else:
            while stack:
                result += stack.pop()
            stack.append(token)
    # 남은 '+'도 result에 추가
    while stack:
        result += stack.pop()

    for i in range(N):
        if result[i].isdecimal():
            stack.append(result[i])
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a + b)

    print(f'#{tc} {stack[0]}')
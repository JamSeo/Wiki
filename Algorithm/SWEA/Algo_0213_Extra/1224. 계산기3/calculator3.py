import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    calculation = input()
    temp = ''
    stack = []

    # 후위 표기식으로 바꾸기
    for token in calculation:
        if token.isdecimal():
            temp += token
        else:
            if not stack:
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
            elif token == '+':
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.append(token)
            elif token == '*':
                stack.append(token)
    else:
        while stack:
            temp += stack.pop()

    # 계산하기
    for token in temp:
        if token.isdecimal():
            stack.append(int(token))
        elif token == '+':
            r = stack.pop()
            l = stack.pop()
            stack.append(l + r)
        elif token == '*':
            r = stack.pop()
            l = stack.pop()
            stack.append(l * r)

    print(f'#{tc} {stack[0]}')

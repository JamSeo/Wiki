# 계산기1

# 받아올 수식 문자열
expression = input()  # 3-2*5+4/2-2
stack = []
# 출력 문자열
result = ''

# 한글자씩 알아보자
for token in expression:
    if token.isdecimal():
        result += token
    else:
        # 첫 연산자
        if not stack:
            # 기록
            stack.append(token)
        # '('는 무조건 push
        elif token == '(':
            stack.append(token)
        # '*' or '/'이면
        elif token in '*/':
            # stack 맨위에 것이 '*' or '/'인지 확인 후
            # 나보다 높은 애가 나올 때 까지 pop
            while stack and stack[-1] in '*/':
                result += stack.pop()
            # 그 다음 나 추가
            stack.append(token)
        # '+' or '-'이면
        elif token in '+-':
            # 더하기 빽는 여는 괄호 보다 낮다
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(token)
        # ')'이면
        elif token == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # 남는 괄호는 버린다

# 남은 계산 연산자
while stack:
    result += stack.pop()  # 325*-42/+2-

for token in result:
    if token.isdecimal():
        stack.append(token)

    elif token == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)

    elif token == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)

    elif token == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)

    elif token == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)

print(stack[0])
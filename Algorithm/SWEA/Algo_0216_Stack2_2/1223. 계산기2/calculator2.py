import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())  # N: 문자열 길이
    input_ = input()  # temp: 문자열 계산식
    stack = []  # 연산자 저장용 스택
    temp = ''

    # Ch1. 후위표기식으로 바꾸기!!
    for token in input_:
        # token이 숫자라면: result에 추가
        if token.isdecimal():
            temp += token
        # 연산자라면
        else:
            # 스택이 비어있으면 바로 추가
            if not stack:
                stack.append(token)
            # 스택에 연산자가 있고, '+-'가 입력되면
            elif token in '+-':
                # 스택 안 연산자 다 result에 더해주고, 본인 추가
                while stack:
                    temp += stack.pop()
                stack.append(token)
            elif token in '*/':
                # '+-'이 나올 때까지 스택 안 연산자 빼주고, 본인 추가
                while stack and stack[-1] in '*/':
                    temp += stack.pop()
                stack.append(token)
            # 이외의 것들은 무시
            else: continue
    # for문 종료 시 stack에 연산자들 result에 더해주기
    else:
        while stack:
            temp += stack.pop()

    # Ch2. 계산하기!!
    for token in temp:
        # 숫자가 나오면 stack에 추가
        if token.isdecimal():
            stack.append(int(token))
        # 연산자가 나오면
        else:
            # 연산할 숫자가 모자라면 에러
            if len(stack) < 2: break
            # 연산 ㄱ
            elif token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(a // b)

    else: print(f'#{tc} {stack[0]}')




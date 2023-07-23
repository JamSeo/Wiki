import sys
sys.stdin = open("sample_input.txt")


T = int(input())  # 테스트케이스
stack = []  # 연산에 사용할 스택

for tc in range(1, T + 1):
    temp = list(input().split())  # 문자열 계산식
    for token in temp:

        # 숫자가 입력되면: push
        if token.isdigit():
            stack.append(int(token))

        # '.'이 입력되면: 결과값 print
        elif len(stack) == 1 and token == '.':
            print(f'#{tc} {stack.pop()}')

        # 연산자를 만나면: 연산 후 결과값 다시 push
        elif len(stack) >= 2 and token in '+-/*':
            if token == '+':
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

        # 연산이 불가능 하면: print('error') / 스택 비우기
        else:
            print(f'#{tc} error')
            stack.clear()
            break
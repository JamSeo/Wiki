import sys
sys.stdin = open("sample_input.txt")

class Stack:
    def __init__(self, arr):
        self.arr = arr
        self.top = -1

    def push(self, item):
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        self.top -= 1
        return self.arr[self.top + 1]

    def peek(self):
        return self.arr[self.top]


T = int(input())

for tc in range(1, T + 1):
    # code: str -- 입력받은 코드
    # stack: Stack -- 코드 개수 만큼의 빈 스택
    code = input()
    stack = Stack([''] * len(code))
    res = 0

    for char in code:  # 반복범위 : code 길이

        # 좌괄호 : push
        if char == '(' or char == '{':
            stack.push(char)

        # 우괄호 ')'
        elif char == ')':
            # 스택의 맨위 값이 '('이면 : '(' pop
            if stack.peek() == '(': stack.pop()
            # '('이 아니라면 : break
            else: break

        # 우괄호 '}'
        elif char == '}':
            # 스택의 맨위 값이 '{'이면 : '{' pop
            if stack.peek() == '{': stack.pop()
            # '{'이 아니라면 : break
            else: break

        # 다른 문자
        else: continue

    # for문 종료 후 stack에 아무것도 남지 않았다면 : 결과값 1 출력
    else:
        if stack.top == -1: res = 1

    print('#{} {}'.format(tc, res))
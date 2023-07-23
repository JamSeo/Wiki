import sys
sys.stdin = open("input.txt")

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


for tc in range(1, 11):  # 테스트케이스: 10
    # N, temp: str -- 문자열 길이, 입력받은 문자열
    # stack: Stack -- 크기 N의 스택
    N, temp = input().split()
    stack = Stack([0] * int(N))

    for num in temp:
        # 입력 숫자와 stack의 꼭대기 값이 다를 경우: push
        if num != stack.peek():
            stack.push(num)
        # 같을 경우: pop
        else: stack.pop()
    
    # for문 종료 후, stackd에 남은 숫자들 그대로 출력
    else:
        password = ''
        for _ in range(stack.top + 1):
            password = stack.pop() + password

    print('#{} {}'.format(tc, password))
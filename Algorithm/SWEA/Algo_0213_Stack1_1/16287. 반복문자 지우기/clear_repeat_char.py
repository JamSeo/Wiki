import sys
sys.stdin = open("sample_input.txt")

class Stack:
    def __init__(self, arr):
        self.arr = arr
        self.top = -1

    def push(self, item):  # item 추가
        self.top += 1
        self.arr[self.top] = item

    def pop(self):  # stack 제일 위의 값 삭제
        self.top -= 1
        return self.arr[self.top + 1]

    def peek(self):  # stack 꼭대기 값이 뭔지?
        return self.arr[self.top]

    def how_many(self):  # stack에 item 몇개 남았는지?
        return self.top + 1


T = int(input())

for tc in range(1, T + 1):
    # temp: str -- 입력 받은 문자열
    # stack: 문자열 수 만큼의 Stack
    temp = input()
    stack = Stack([''] * len(temp))

    for char in temp: # 반복범위 : 입력된 문자열

        # 입력값 == 스택 꼭대기 값 : 스택 꼭대기 값 제거
        if char == stack.peek():
            stack.pop()

        # 입력값 != 스택 꼭대기 값 : 문자열 추가
        elif char != stack.peek():
            stack.push(char)

    # for문 종료 후 남아있는 문자열 수 출력
    else:
        res = stack.how_many()
        print('#{} {}'.format(tc, res))
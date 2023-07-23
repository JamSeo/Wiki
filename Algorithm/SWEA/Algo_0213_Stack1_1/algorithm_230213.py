# 괄호 검사
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

    def is_empty(self):
        return self.top == -1

    def peek(self):
        return self.arr[self.top]


data = input()
stack = Stack([0] * len(data))
result = -1

for i in range(len(data)):
    # 비어있는 상태에서 '('가 들어올 때
    if stack.top == -1 and data[i] == '(':
        stack.push(data[i])
    # '('이면 push
    elif data[i] == '(':
        stack.push(data[i])
    # ')'이면 바로 전 '('를 pop
    elif data[i] == ')':
        if stack.peek() == '(':
            stack.pop()
        # 바로 전 '('가 없으면 break
        else: break
    # 비어있는 상태에서 ')'가 들어올 때 break
    elif  stack.top == -1 and data[i] == ')':
        break
    # 그외... ' '가 들어온다거나..
    else: break

# for - else는 break 없이 반복이 종료된 for에 대해서 else 실행
else: # 다 검사 한거
    if stack.is_empty():
        result = 1

print(result)


















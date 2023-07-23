import sys
sys.stdin = open("input.txt")

class Stack:
    def __init__(self, num, sqr):
        self.num = num  # num: 제곱해줄 숫자
        self.top = sqr  # sqr: 제곱수

    def involution(self):
        # top이 0이되면 : 1 반환
        if self.top == 0:
            return 1
        # top이 0이 될때까지 sqr만큼  num을 곱해줌
        else:
            self.top -= 1
            return self.num * Stack.involution(self)

for _ in range(10):
    tc = input()
    # stack : Stack -- num, sqr 저장한 클래스
    num, sqr = map(int, input().split())
    stack = Stack(num, sqr)

    ans = stack.involution()
    print(f'#{tc} {ans}')
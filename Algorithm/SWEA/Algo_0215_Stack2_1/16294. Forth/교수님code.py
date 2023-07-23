import sys
sys.stdin = open("sample_input.txt")

# 좌항 우항 연산자 계산
def calculate(left, right, operator):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left + right
    elif operator == '/':
        return left // right
    # 다른 연산자는 출제자의 잘못
    else:
        raise ValueError(f"wrong operator: {operator}")

# 연산자 묶음
OPS = "+-*/"


T = int(input())

for tc in range(1, T + 1):
    expression = input().split()
    dig_stack = []

    for token in expression:
        # 수식 입력 종료
        if token == '.':
            if len(dig_stack) == 1:
                print(f'#{tc} {dig_stack.pop()}')
            else:
                print(f'#{tc} error')
        # 연산자 입력
        elif token in OPS:
            # 연산할 숫자가 모자른다
            if len(dig_stack) < 2:
                print(f'#{tc} error')
                break
            # 아니라면 계산한다.
            operand_right = dig_stack.pop()
            operand_left = dig_stack.pop()
            # 계산 결과는 스택으로
            dig_stack.append(int(calculate(operand_left, operand_right, token)))
        # 위가 아니면 다 숫자다.
        else:
            dig_stack.append(int(token))
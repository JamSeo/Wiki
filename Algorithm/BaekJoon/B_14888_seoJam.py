# 저는 순열로 풀어서 실행 시간이 2788ms 나오는데..
# 구글에 DFS 코드 있어서 보니까 112ms 뜨네요. 심정이 매우 처량합니다...

from itertools import permutations

def calculator(operator, num1, num2):  # 계산 함수
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        if num1 < 0:
            return -(abs(num1) // num2)
        else:
            return num1 // num2

n = int(input())
nums = list(map(int, input().split()))  # 숫자열
cnt = list(map(int, input().split()))   # 연산자별 개수
cal = ["+", "-", "*", "/"]

# operators: n-1개의 연산자 리스트
operators = []
temp = ''
for i in range(4):
    if cal[i] * cnt[i]:
        temp += cal[i] * cnt[i]
operators = list(temp)

# operators로 순열 만들기
permute = list(permutations(operators, n-1))

# 계산하기
max_, min_ = -1e9, 1e9
res = nums[0]
for i in range(len(permute)):
    for j in range(n-1):
        res = calculator(permute[i][j], res, nums[j+1])
    # 계산 끝나면?
    max_ = max(max_, res)
    min_ = min(min_, res)
    res = nums[0]

print(max_, min_, sep='\n')
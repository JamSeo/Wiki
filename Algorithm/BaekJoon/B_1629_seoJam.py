# Googling 100%
# 분할정복을 이용한 거듭제곱
# 합동식
def DaC(a, b, c):
    if b == 1:          # [0] Base
         return a % c

    temp = DaC(a, b // 2, c)

    if b % 2:           # [1] b가 홀수?
        return temp * temp * a % c
    else:               # [2] b가 짝수?
        return temp * temp % c


a, b, c = map(int, input().split())

print(DaC(a, b, c))

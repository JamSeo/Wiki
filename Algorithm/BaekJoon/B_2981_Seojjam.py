# /////////////////// 내 풀이 ///////////////////
# 입력된 첫 숫자(6)를 2부터 해당숫자까지 나눴을 때의 나머지를 저장한 리스트를 생성
# 이때, 리스트 idx(2~6)는 6을 나눠줬던 숫자 (단 list[0], list[1]에는 각각 -1을 저장)
# #=> [-1, -1, 0, 0, 2, 1, 0]

# 다음 숫자(34, 38)를 입력받고 2~6으로 나눠준 뒤, 그 나머지를 위 list 값들과 비교
# list와 나머지가 같으면 pass, 다르면 해당 list값을 -1로 바꿔줌
# #=> [-1, -1, 0, -1, 2, -1, -1]

# 마지막으로 list에서 값이 -1이 아닌 idx만 출력; 2 4

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())  # N: 종이에 적은 숫자의 개수
min_num = int(input())  # 6
# res: [] -- 6을 2~6까지의 숫자로 나눈 나머지; [-1, -1, 0, 0, 2, 1, 0]
res = [-1, -1] + [min_num % n for n in range(2, min_num+1)]

for i in range(N - 1):
    num = int(input())  # 34, 38
    # 입력된 숫자를 2~6까지의 숫자로 나눈 나머지와 res[] 값을 차례로 비교
    # 이때 나머지 값이 같지 않다면 res[] 값을 -1로 바꿔줌
    for n in range(2, min_num+1):
        if num % n != res[n]:
            res[n] = -1
# ans : [] -- res[]에서 -1이 아닌 값들의 idx; [2, 4]
ans = [idx for idx in range(min_num-1) if res[idx] != -1]
print(*ans)  #=> 2 4



# /////////////////// Googling 'ㅎ'*3 ///////////////////
# A = Ma + R, B = Mb + R, C = Mc + R 일때
# B - A = M(b - a),
# C - B = M(c - b)이므로
# 입력된 숫자들의 차에서 최대공약수와 그 공약수들을 구해주면 됨.

import math

N = int(input())  # N: int -- 종이에 적은 숫자의 개수
nums = [int(input()) for _ in range(N)]  # nums: [] -- N개의 숫자들
ans = []

# interval: [] -- nums 숫자들의 차
interval = []
for i in range(1, N):
    interval.append(nums[i] - nums[i-1])

# interval 값들의 최대공약수 구하기; gcd()
temp = interval[0]
for i in range(1, len(interval)):
    temp = math.gcd(temp, interval[i])

# 최대공약수의 공약수들 구하기
# range 범위: 2부터 최대공약수의 제곱근까지 (반복횟수를 줄이기 위해)
# cf. 18 % 2 == 0이면 2도 약수, (18 // 2 ==)9도 약수임을 이용
for i in range(2, int(temp**0.5) + 1):
    if not temp % i:
        ans.append(i)
        ans.append(temp // i)
ans.append(temp)
ans = [set(ans)]  # 중복된 공약수 제거; set()
ans.sort()

print(*ans)

# # /////////////////// 내 풀이 ///////////////////
# # ps. 런타임 에러(OverflowError)의 향연

# import sys
# input = sys.stdin.readline
#
# def factorial(num):  # 팩토리얼 함수
#     res = 1
#     for i in range(1, num + 1): res *= i
#     return res
#
# def Combination(n, r):  # 조합 함수
#     res = factorial(n) / factorial(r) / factorial(n - r)
#     return int(res)
#
#
# N, K = map(int, input().split())
# print(Combination(N, K) % 10007)  # 이항계수를 10,007로 나눈 나머지 출력



# /////////////////// Googling ///////////////////
# ps. 역시 세상은 쉽지 않았고 파스칼의 삼각형을 이용하게 되었습니다.
# N + 1 층까지의 파스칼 삼각형의 2차원 []를 만들고 Combination(N, K) % 10007을 구해줌.

N, K = map(int, input().split())
tri = []  # tri: 2차원 [] -- 파스칼의 삼각형

for i in range(N + 1):
    tri.append([1] * (i + 1))

for i in range(2, N + 1):
    for j in range(1, i):
        tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

print(tri[N][K] % 10007)


import sys
input = sys.stdin.readline

def factorial(num):  # 팩토리얼 함수
    res = 1
    for i in range(1, num + 1): res *= i
    return res

def Combination(n, r):  # 조합 함수
    return factorial(n) / factorial(r) / factorial(n - r)


T = int(input())  # 테스트케이스

for _ in range(T):
    # 주어진 조건하에 다리를 지을 수 있는 경우의 수: M개 중 N개의 조합
    # ; Combination(M, N)

    N, M = map(int, input().split())  # N, M : 강의 서쪽과 동쪽에 있는 사이트의 수
    print(int(Combination(M, N)))

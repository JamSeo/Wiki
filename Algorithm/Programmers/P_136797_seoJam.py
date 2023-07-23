# 구글링.. 쩝
# 왼쪽과 오른쪽 손가락 중 더 가까이에 있는 손가락으로 숫자를 누르는 그리디 방식으로 풀었는데 틀림
from collections import defaultdict
import sys
sys.setrecursionlimit(200000)
# cache[i][(left, right)]
# i번째 숫자를 누른 상태에서
# 왼손이 left, 오른손이 right에 있는 경우 최소 가중치
cache = defaultdict(dict)

# 번호별 가중치
keyboard = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]
]


def dfs(i, left, right, numbers):

    if i == len(numbers):
        return 0

    if (left, right) in cache[i]:
        return cache[i][(left, right)]

    weight = 1e9
    num = numbers[i]

    # 왼손 클릭
    if num != right:
        weight = min(weight, dfs(i+1, num, right, numbers) + keyboard[left][num])
    # 오른손 클릭
    if num != left:
        weight = min(weight, dfs(i+1, left, num, numbers) + keyboard[right][num])

    # 캐쉬에 현재값 가중치 저장
    cache[i][(left, right)] = weight

    return weight


def solution(numbers):
    numbers = list(map(int, numbers))

    return dfs(0, 4, 6, numbers)

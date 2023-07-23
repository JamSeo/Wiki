# 동전 뒤집는 함수
def flip(coin):
    return 1 - coin


def solution(beginning, target):
    if beginning == target:
        return 0

    cnt1 = 0
    n, m = len(target), len(target[0])
    temp = [[0] * m for _ in range(n)]

    # [1] 각 동전이 뒤집어진 횟수 저장 (0: 짝수번 / 1: 홀수번)
    for i in range(n):
        for j in range(m):
            temp[i][j] = 1 if beginning[i][j] != target[i][j] else 0

    # [2] temp의 0번째 행과 나머지 행들 일치시키기
    for i in range(1, n):
        if temp[i][0] != temp[0][0]:
            temp[i] = list(map(flip, temp[i]))
            cnt1 += 1
        # 이때, 뒤집은 행과 0번째 행이 같지 않다면? 불가능
        if temp[i] != temp[0]:
            return -1

    # [3] temp에서 1로만 구성된 열의 개수 더해주기
    cnt2 = temp[0].count(1)
    answer1 = cnt1 + cnt2
    # 이때, 반대의 경우도 해가 될 수 있음..!
    answer2 = (n - cnt1) + (m - cnt2)

    return min(answer1, answer2)


# print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))
# print(solution([[0, 0, 1], [1, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 0, 0], [1, 0, 0]]))
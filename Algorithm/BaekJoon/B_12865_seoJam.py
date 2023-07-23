# 구글링 100% [출처: https://claude-u.tistory.com/208]
# 쉬운줄 알았다가 뜨겁게 대였습니다.
# 그래도 'fucking 냅색 알고리즘'에 대해서 공부할 수 있어서 행복했습니다.

# Knapsack Problem
# [1] (행:가방무게(1~K), 열:물건개수(1~N))의 전체 0으로 저장된 2차리스트 만들기
# [2] for-for 반복문으로 리스트에 값 채워줌
# [3] '현재물건 가치' + 리스트[이전물건][현재가방 무게 - 현재물건 무게]  vs  리스트[이전물건][현재가방 무게]
# [4] 과정[3]에서 더 높은 값을 리스트에 저장
# [5] 마지막, 리스트[N][K] 값 출력. 끝.

# 이제, 이대로 구현 해보겠습니당

if __name__ == '__main__':
    # n: 물품의 수, k: 버티는 최고 무게
    n, k = map(int, input().split())
    item = []
    for _ in range(n):
        weight, value = map(int, input().split())
        item.append([weight, value])
    # [1]
    knapsack = list([0] * (k+1) for _ in range(n+1))
    # [2]
    for i in range(1, n+1):
        # now_weight: 현재물건 무게, now_value: 현재물건 가치
        now_weight, now_value = item.pop()

        for j in range(1, k+1):
            if now_weight > j:
                knapsack[i][j] = knapsack[i-1][j]
    # [3], [4]
            else:
                knapsack[i][j] = max(now_value + knapsack[i-1][j-now_weight], knapsack[i-1][j])

    print(knapsack[n][k])

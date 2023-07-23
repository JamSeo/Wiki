import sys
sys.stdin = open('sample_input.txt')

# k: 범위 크기, houses: 집좌표, N: city_size
def check_profit(k, houses, city_size, margin):
    result = 0
    cost = k**2 + (k-1)**2

    for i in range(city_size):
        for j in range(city_size):
            house_count = 0
            for house_y, house_x in houses:
                # 현위치에서 도달 가능한 곳에 집이 있다면?
                if abs(i - house_y) + abs(j - house_x) <= k - 1:
                    house_count += 1

            profit = house_count * margin - cost
            # 이득이 남고 집 개수가 최댓값일 때
            if profit >= 0 and house_count > result:
                result = house_count
    return result


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 집 좌표 저장
    houses = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if line[j]:
                houses.append((i, j))

    result = 0
    for k in range(N + 2, 0, -1):
        result = max(check_profit(k, houses, N, M), result)

    print(f'#{tc} {result}')

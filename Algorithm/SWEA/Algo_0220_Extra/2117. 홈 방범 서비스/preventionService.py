import sys
sys.stdin = open("sample_input.txt")

# K 크기별 운영 비용
cost = [K * K + (K - 1) * (K - 1) for K in range(40)]

def check(K):
    # 현 위치에서 K거리 안에 집 개수 세어주기
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for house_i, house_j in houses:
                if abs(house_i - i) + abs(house_j - j) <= K -1:
                    cnt += 1
            # 집 최대 개수 구하기
            if M * cnt >= cost[K] and cnt > max_cnt:
                max_cnt = cnt
    return max_cnt


T = int(input())

for tc in range(1, T + 1):
    # N: 도시의 크기, M: 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    # 집 좌표 찾아서 저장
    houses = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            if temp[j]:
                houses.append((i, j))
    # K값을 줄여가며 최대 집 개수 구하기
    max_house = 0
    for K in range(N+2, 0, -1):
        max_house = max(max_house, check(K))

    print(f'#{tc} {max_house}')
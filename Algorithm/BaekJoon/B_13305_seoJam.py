if __name__ == '__main__':
    n = int(input())                        # n: 도시 개수
    dis = list(map(int, input().split()))   # dis: 도시간 거리
    oil = list(map(int, input().split()))   # oil: 주유소 가격
    ans = i = j = 0                         # i: oil의 idx, j: dis의 idx

    while i < n - 1:
        min_oil = oil[i]                    # min_oil: 현재 주유소 가격
        cnt = 1                             # cnt: 이동 횟수
        # [1] 이동 위치가 n보다 작고, 현재 주유소 가격이 이동후 주유소 가격보다 작을 때까지 이동
        while i+cnt < n and min_oil <= oil[i+cnt]: cnt += 1
        # [2] 이동이 끝나면, 출력값에 (이동한 거리*현재 주유소 가격) 더해줌
        ans += min_oil * sum(dis[j:j+cnt])
        j += cnt
        i += cnt

    print(ans)
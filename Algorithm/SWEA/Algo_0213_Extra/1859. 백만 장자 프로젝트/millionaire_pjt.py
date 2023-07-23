import sys
sys.stdin = open("input.txt")


T = int(input())  # 테스트케이스

for tc in range(1, T + 1):
    # N: int -- 매매가를 예측 가능한 일 수
    # price: [] -- 매매가 리스트
    N = int(input())
    price = list(map(int, input().split()))

    margin = 0  # 마지막에 출력할 최대 이익
    max_price = price[-1]  # 리스트 가장 마지막 값을 max_price로 설정

    # 반복범위: idx (N-2 -> 0)
    for i in range(N-2, -1, -1):
        # 매매값이 max_price 보다 크거나 같으면: 해당 값을 max_price로 저장
        if max_price <= price[i]:
            max_price = price[i]
        # max_price 보다 작으면:  차이값을 margin에 더해줌
        else:
            margin += max_price - price[i]

    print(f'#{tc} {margin}')
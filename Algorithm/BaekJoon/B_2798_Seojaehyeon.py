# N : int -- 카드의 개수 (3 ≤ N ≤ 100)
# M : int -- 딜러가 부를 숫자(10 ≤ M ≤ 300,000)
# card : [] -- 카드에 쓰여있는 수
N, M = map(int, input().split())
cards = list(map(int, input().split()))


result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):

            sum_card = cards[i] + cards[j] + cards[k]

            if sum_card > M:  # 카드합이 M보다 크면 계속 for문 진행
                continue
            else:  # 카드합이 M보다 같거나 작으면 result에 저장 후
                if result < sum_card:
                    result = sum_card

print(result)
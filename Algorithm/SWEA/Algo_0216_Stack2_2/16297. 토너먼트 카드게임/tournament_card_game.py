import sys
sys.stdin = open("sample_input.txt")

# [1] 그룹을 더 안쪼개질 때까지 계속 쪼개
# [2] 연산을 통해서 한 차례씩 하나로 모아
# [3] 마지막 winner 출력

def split(arr, l, r):
    if l == r:
        return l
    mid = (l + r) // 2
    left = split(arr, l, mid)
    right = split(arr, mid + 1, r)
    return battle(arr, left, right)

def battle(arr, l, r):
    if not (arr[r] - arr[l] + 2) % 3:
        return r
    else:
        return l


T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # N : 인원수
    card = list(map(int, input().split()))

    winner = split(card, 0, N-1)

    print(f'#{tc} {winner + 1}')
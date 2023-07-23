import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))
    guest.sort()
    ans = 'Impossible'
    time = 0

    while len(guest) != 0:
        time += M

        if guest[0] < time:
            break
        else:
            for _ in range(K):
                guest.pop(0)
                if not len(guest):
                    ans = 'Possible'
                    break

    print(f'#{tc} {ans}')
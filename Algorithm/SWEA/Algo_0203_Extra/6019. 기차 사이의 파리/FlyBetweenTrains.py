import sys
sys.stdin = open("s_input.txt")

T = int(input())  # 테스트케이스: 1
distance = []

for tc in range(1, T + 1):
    # D: 두 기차 전면부 사이의 거리
    # A: 기차 A의 속력
    # B: 기차 B의 속력
    # F: 파리의 속력
    D, A, B, F = map(int, input().split())

    distance.append(f'#{tc} {D / (A + B) * F}')

print(*distance)
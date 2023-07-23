import sys
sys.stdin = open("sample_input.txt")

# [1] separate()
# [2] battle()
# [3] return battle()

# data 전체카드, left 왼쪽 인덱스(0), right 오른쪽 인덱스(N-1)
def separate(data, left, right):
    if left == right:
        return left

    mid = (left + right) // 2

    left_group = separate(data, left, mid)
    right_group = separate(data, mid+1, right)
    return battle(data, left_group, right_group)


def battle(data, left, right):
    result = (data[left] - data[right]) % 3
    if result == 2:  # 왼쪽이 지는 경우; -1 % 3 = 2 % 3 = 2
        return right
    else:            # 오른쪽이 지는 경우
        return left


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    res = separate(data, 0, N - 1)

    print(f'#{tc} {res + 1}')  # 시작학생 번호가 1번이기 때문





















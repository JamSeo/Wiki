import sys
sys.stdin = open('input.txt')

def max(list):  # 함수 max 정의
    i_max = list[0]
    for i in list:
        if i_max < i:
            i_max = i
    return i_max

T = 10  # 테스트 케이스 : 10

for tc in range(1, T + 1):
    N = int(input())  # 건물의 개수 N (4 ≤ N ≤ 1000)
    buildings = list(map(int, input().split()))  # 건물높이 리스트 (0 ≤ 각 건물의 높이 ≤ 255)

    view = 0  # 조망권이 확보된 칸 수 : 0

    for i in range(2, N - 1):  # for문 범위 : 건물높이 값이 존재하는 idx; height[2:-1]

                near = buildings[(i - 2):(i + 3)]  # 리스트 slice : i-2부터 i+2까지

                if buildings[i] == max(near):  # slice된 리스트에서 i값이 가장 크다면,
                    near.remove(buildings[i])
                    view += (buildings[i] - max(near))  # view += (i값 - 주변 두번째 건물높이값)

    print("#{} {}".format(tc, view))

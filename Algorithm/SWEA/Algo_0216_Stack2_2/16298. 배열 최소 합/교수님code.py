import sys
sys.stdin = open("sample_input.txt")

# selected 리스트에 각 idx에 몇번째를 선택했는지 저장한다.
# 저장이 안된 항목은 아직 선택하지 않은 것
# 매번 DFS 마다 selected와 입력 NxN 행렬을 가지고 합을 구해보고,
# 여태까지 나온 결과 중 제일 작은 것보다 커지면,
# 그때 return

# arr 데이터, selected 고른 정보
def claculate_sum(arr, selected):
    temp_sum = 0
    for i in range(len(selected)):
        # seleted[i]에는 i번째 줄에서 몇번째 칸을 골랐는지 저장되어있다.
        temp_sum += arr[i][selected[i]]
    return temp_sum


# arr 데이터, selected 각 줄의 몇번째를 선택했는지, row 현재 찾아봐야 될 줄, size 데이터의 크기(N)
def test_sum(arr, selected, row, size):
    # ///////////// 백트래킹 부분 ////////////
    global min_sum
    temp_sum = claculate_sum(arr, selected)
    if temp_sum > min_sum:
        return
    # /////////////////////////////////////
    if row == size:
        # arr에서 selected를 기반으로 현재 최소를 구하자.
        temp_sum = claculate_sum(arr, selected)
        min_sum = min(min_sum, temp_sum)
        return

    # i: 0 ~ size-1
    for i in range(size):
        # 이미 선택한 적 있는 인덱스다
        if i in selected:
            # 다음 인덱스 검사
            continue
        # 이번 줄에서 선택해서 다음 줄로 넘기자
        selected.append(i)
        test_sum(arr, selected, row+1, size)
        selected.pop()


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9 * N

    # 각 idx에는 해당하는 줄에서 선택한 idx가 담긴다.
    selected = []
    row = 0
    test_sum(arr, selected, row, N)
    print(f'#{tc} {min_sum}')
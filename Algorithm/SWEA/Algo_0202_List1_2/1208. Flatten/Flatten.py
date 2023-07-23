import sys
sys.stdin = open("input.txt")

def top(lst):  # 최고 높이의 상자 idx 반환 함수
    top_lst = lst[0]
    top_idx = 0
    for idx in range(len(lst)):
        if top_lst < lst[idx]:
            top_lst = lst[idx]
            top_idx = idx
    return top_idx

def bottom(lst):  # 최저 높이의 상자 idx 반환 함수
    bottom_lst = lst[0]
    bottom_idx = 0
    for idx in range(len(lst)):
        if bottom_lst > lst[idx]:
            bottom_lst = lst[idx]
            bottom_idx = idx
    return bottom_idx


T = 10  # 테스트케이스 : 10

for tc in range(1, T + 1):

    dump = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 상자 높이값 []

    for i in range(dump):
        top_idx = top(boxes)  # 최고 높이의 상자 idx
        boxes[top_idx] -= 1  # 상자 1개 빼기

        bottom_idx = bottom(boxes)  # 최저 높이의 상자 idx
        boxes[bottom_idx] += 1  # 상자 1개 더하기

    # for문 이후 최종 최고/최소의 상자 idx 확인
    top_idx = top(boxes)
    bottom_idx = bottom(boxes)

    # 최고/최소 상자의 높이차
    gap = boxes[top_idx] - boxes[bottom_idx]
    print("#{} {}".format(tc, gap))
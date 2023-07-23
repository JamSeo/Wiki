import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    max_drop = 0

    for idx in range(N -1):
        box_height = boxes[idx]

        tmp_drop = 0
        for j in range(idx +1, N):
            if box_height > boxes[j]:
                tmp_drop += 1

        print(tmp_drop)
        if max_drop < tmp_drop:
            max_drop = tmp_drop

    print("#{} {}".format(test_case, max_drop))

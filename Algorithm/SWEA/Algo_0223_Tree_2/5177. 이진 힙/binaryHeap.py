import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    heap = [0]

    for num in temp:
        heap.append(num)
        child = len(heap) - 1
        parent = child // 2
        while parent > 0 and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2

    ans = 0
    child = len(heap) - 1
    parent = child // 2
    ans += heap[parent]
    while parent > 0:
        parent //= 2
        ans += heap[parent]
    print(f'#{tc} {ans}')
import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    heap = [0]
    family_tree = [0] * 1001    # 족보; 해당 인자의 부모 idx를 저장

    for _ in range(N):
        temp = input().split()
        if len(temp) == 4:
            heap.append(temp[1])
            family_tree[int(temp[2])] = int(temp[0])
            family_tree[int(temp[3])] = int(temp[0])
        else:
            heap.append(temp[1])

    while len(heap) != 2:
        child = len(heap) - 1
        parent = family_tree[child]
        r = int(heap.pop(child))
        l = int(heap.pop(child - 1))

        if heap[parent] == '+':
            heap[parent] = l + r
        elif heap[parent] == '-':
            heap[parent] = l - r
        elif heap[parent] == '*':
            heap[parent] = l * r
        elif heap[parent] == '/':
            heap[parent] = l // r

    print(f'#{tc} {heap.pop()}')
import sys
sys.stdin = open("sample_input.txt")

# 전위 순회
def preorder(tree, node):
    global count
    if node:
        # 나
        count += 1
        # 왼쪽
        preorder(tree, tree[node][0])
        # 오른쪽
        preorder(tree, tree[node][1])


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    tree = [[0] * 2 for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    count = 0

    # 트리 만들기~~
    for i in range(E):
        parent, child = temp[2 * i], temp[2 * i + 1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    preorder(tree, N)
    print(f'#{tc}', count)



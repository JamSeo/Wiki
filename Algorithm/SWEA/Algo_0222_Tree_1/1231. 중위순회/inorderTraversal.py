import sys
sys.stdin = open("input.txt")

# 중위 순회(L - V - R)
def inorder(tree, node):
    global ans
    if node != 0:   # 아닐 때는 순회 X
        # 왼쪽
        inorder(tree, tree[node][0])
        # 나
        ans.append(tree[node][2])
        # 오른쪽
        inorder(tree, tree[node][1])


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 1)]
    ans = []

    for _ in range(N):
        data = input().split()
        node, alp = int(data[0]), data[1]
        tree[node][2] = alp

        if len(data) == 4:
            left = int(data[2])
            right = int(data[3])
            tree[node][0] = left
            tree[node][1] = right
        elif len(data) == 3:
            left = int(data[2])
            tree[node][0] = left

    inorder(tree, 1)
    print(f'#{tc}', ''.join(ans))


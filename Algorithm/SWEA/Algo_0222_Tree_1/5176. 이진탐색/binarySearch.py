import sys
sys.stdin = open("sample_input.txt")

# 중위 순회(L - V - R)
def inorder(tree, node):
    if node != 0:
        inorder(tree, tree[node][0])
        ans.append(node)  # 본인이 탐색되면 ans에 저장
        inorder(tree, tree[node][1])


T = int(input())

for tc in range(1, T + 1):
    V = int(input())
    E = V - 1
    ans = []  # 탐색 순서 리스트

    # tree: [left자식, right자식]
    tree = list([0] * 2 for _ in range(V + 1))
    for i in range(1, E):
        # left 자식 저장
        if 2 * i <= V and not tree[i][0]:
            tree[i][0] = 2 * i
            # right 자식 저장
            if 2 * i + 1 <= V and not tree[i][1]:
                tree[i][1] = 2 * i + 1

    inorder(tree, 1)
    # print(ans)
    print(f'#{tc}', ans.index(1) + 1, ans.index(V//2) + 1)
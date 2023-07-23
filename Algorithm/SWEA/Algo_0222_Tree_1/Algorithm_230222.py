# 정점의 개수가 13일 때 전위순회하는 순서

# 전위 순회(V - L - R)
# node는 시작점 또는 현재점
def preorder(tree, node):
    if node != 0:   # 아닐 때는 순회 X
        # 나
        print(f'{node}', end=' ')
        # 왼쪽
        preorder(tree, tree[node][0])
        # 오른쪽
        preorder(tree, tree[node][1])

# 중위 순회(L - V - R)
def inorder(tree, node):
    if node != 0:   # 아닐 때는 순회 X
        # 왼쪽
        inorder(tree, tree[node][0])
        # 나
        print(f'{node}', end=' ')
        # 오른쪽
        inorder(tree, tree[node][1])

# 후위 순회(L - R - V)
def postorder(tree, node):
    if node != 0:   # 아닐 때는 순회 X
        # 왼쪽
        postorder(tree, tree[node][0])
        # 오른쪽
        postorder(tree, tree[node][1])
        # 나
        print(f'{node}', end=' ')


V = 13      # 노드의 개수
E = V - 1   # 간선의 개수
# 0~V 까지의 노드의 [왼쪽 자식, 오른쪽 자식, 부모] 정보
# 만약 [l, r, p]의 값 중 0은 없다는 의미
tree = list([0 for _ in range(3)] for _ in range(V + 1))

temp = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
for i in range(E):
    # parent, child로 구분
    parent, child = temp[i * 2], temp[i * 2 + 1]

    # 왼쪽 자식이 없다면
    if not tree[parent][0]:
        tree[parent][0] = child
    # 오른쪽 자식은 없어야됨
    else:
        tree[parent][1] = child
    # 부모 정보도 업데이트
    tree[child][2] = parent

print(tree)
preorder(tree, 1)
print()
inorder(tree, 1)
print()
postorder(tree, 1)
print()
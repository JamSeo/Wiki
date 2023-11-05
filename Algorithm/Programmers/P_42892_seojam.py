import sys
from copy import deepcopy

# 재귀 깊이 limit 설정 (nodeinfo의 길이가 1 이상 10,000 이하이므로!!!)
sys.setrecursionlimit(10**4)


# 부모노드의 X축 기준 좌우로 자식 노드를 나누는 함수
def split_nodes(nodeinfo):
    parent = nodeinfo.pop(0)
    leftNodes, rightNodes = [], []

    for node in nodeinfo:
        if parent[0] > node[0]:
            leftNodes.append(node)
        else:
            rightNodes.append(node)

    return parent, leftNodes, rightNodes


# 전위 순회
def preorder(nodeinfo, answer):
    if not nodeinfo:
        return

    parent, leftNodes, rightNodes = split_nodes(nodeinfo)
    answer.append(parent[2])
    preorder(leftNodes, answer)
    preorder(rightNodes, answer)


# 후위 순회
def postorder(nodeinfo, answer):
    if not nodeinfo:
        return

    parent, leftNodes, rightNodes = split_nodes(nodeinfo)
    postorder(leftNodes, answer)
    postorder(rightNodes, answer)
    answer.append(parent[2])


def solution(nodeinfo):
    # 0. nodeinfo에 노드번호 저장
    for idx, node in enumerate(nodeinfo):
        node.append(idx + 1)

    # 1. y-x 순 nodeinfo 정렬
    nodeinfo.sort(key=lambda node: (-node[1], node[0]))

    # 2. 전위 순회
    preanswer = []
    preorder(deepcopy(nodeinfo), preanswer)

    # 3. 후위 순회
    postanswer = []
    postorder(deepcopy(nodeinfo), postanswer)

    return [preanswer, postanswer]


print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
)

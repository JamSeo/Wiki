import sys
sys.stdin = open("input.txt")

# 후위순회 함수 (L - R - V)
# tree는 트리, node는 정점 번호 (또는 idx)
def post_order(tree, node):
    # 숫자만 있는 단말 노드
    if len(tree[node]) == 2:
        # 숫자를 반환
        return tree[node][1]
    # 좌우 자식과 연산자가 있는 노드
    else:
        # 왼쪽 자식 노드(또는 subtree)의 결과가 왼쪽 피연산자.
        left_operand = post_order(tree, tree[node][2])
        # 오른쪽도 동일
        right_operand = post_order(tree, tree[node][3])

        # 계산하기
        if tree[node][1] == '+':
            return left_operand + right_operand
        elif tree[node][1] == '-':
            return left_operand - right_operand
        elif tree[node][1] == '*':
            return left_operand * right_operand
        else:
            return left_operand // right_operand


for test_case in range(1, 11):
    N = int(input())
    expression_tree = [input().split() for _ in range(N)]

    # 각 정점에 적용
    for expression_node in expression_tree:
        i = 0
        # 정점이 가진 정보들이
        while i < len(expression_node):
            # 숫자 정보라면
            if expression_node[i].isdecimal():
                # 정수로 변환
                expression_node[i] = int(expression_node[i])
            # 다음글자
            i += 1

    # 첫자리 0
    expression_tree = [0] + expression_tree
    print(f'#{test_case} {post_order(expression_tree, 1)}')
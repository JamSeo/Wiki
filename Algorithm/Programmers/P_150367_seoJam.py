def tree_check(tree, idx):
    global answer
    # [1] 이미 이진트리 표현 불가 판정이 났거나, 리프노드일 때
    if answer[idx] == 0 or len(tree) == 1:
        return
    # [2] 검사: 부모노드가 0인데 자식노드 중 1이 있으면 X
    parent = len(tree) // 2
    child1, child2 = parent // 2, parent + parent // 2 + 1
    if tree[parent] == '0':
        if tree[child1] == '1' or tree[child2] == '1':
            answer[idx] = 0  # 이진트리 표현 불가 판정
            return
    # [3] 부모노드(루트) 기준 좌우 서브트리 검색
    tree_check(tree[:parent], idx)
    tree_check(tree[parent + 1:], idx)


def solution(numbers):
    global answer
    N = len(numbers)
    answer = [1] * N

    for idx in range(N):
        # [1] 10진수 -> 2진수로 변환
        bin_num = bin(numbers[idx])[2:]
        # [2] 2진수 -> 포화 이진트리로 변환
        n = 0
        len_tree = 2**n
        while len_tree < len(bin_num):
            n += 1
            len_tree += 2**n
        tree = '0'*(len_tree-len(bin_num)) + bin_num  # 더미노드 추가
        # [3] 포화 이진트리 검사 시작
        tree_check(tree, idx)

    return answer
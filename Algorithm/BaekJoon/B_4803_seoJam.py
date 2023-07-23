# dfs(): 자기(me)의 자식노드(child)를 탐색하며
# 1. 자기 부모(parent)와 같은 번호의 자식 노드는 건너뛰기
# 2. 부모와 다른 번호의 노드인데, 이미 방문한 노드면 싸이클로 판정

def dfs(parent, me):
    visited[me] = True  # 방문 처리

    for child in tree[me]:
        if parent == child:   # 1
            continue
        elif visited[child]:  # 2
            return False

        if not dfs(me, child):  # 위의 조건으로 예하 재귀 함수가 싸이클로 판정되면, False 반환
            return False
    return True


tc = 0
while True:
    tc += 1
    v, e = map(int, input().split())
    # [1] "0, 0" 입력되면 break
    if (v, e) == (0, 0):
        break
    tree = list([] for _ in range(v+1))
    visited = [0] * (v+1)
    answer = 0

    # [2] 트리 만들기
    for _ in range(e):
        v1, v2 = map(int, input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)

    # [3] dfs
    for node in range(1, v+1):
        if not visited[node]:
            if dfs(0, node):  # dfs(parent, me); 처음 부모노드를 0번으로 탐색 시작
                answer += 1

    if not answer:
        print(f"Case {tc}: No trees.")
    elif answer == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {answer} trees.")
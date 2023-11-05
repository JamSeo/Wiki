import sys
sys.setrecursionlimit(3 * 10**5)
from collections import defaultdict

def dfs(a, tree, parent, me, answer):
    # 자식 탐색
    for child in tree[me]:
        # 부모 노드 pass
        if child == parent:
            continue
        dfs(a, tree, me, child, answer)
    
    # 탐색이 완료되면 부모에게 상납
    a[parent] += a[me]
    answer[parent] += abs(a[me])
    # print(me, answer)

def solution(a, edges):
    answer = [0 for _ in a]
    
    # [0] 모든 정점의 가중치 합이 0이 아닌 경우 
    if sum(a) != 0:
        return -1
    
    # [1] 트리 만들기
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # [2] dfs로 트리 끝부터 가중치 끌어모으기
    dfs(a, tree, 0, 0, answer)
        
    return sum(answer)
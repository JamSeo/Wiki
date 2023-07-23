from collections import deque

def DFS(tree, start):
    global visited
    visited[start] = True
    print(start, end=' ')
    for child in range(1, v+1):
        if not visited[child] and tree[start][child]:
            DFS(tree, child)


def BFS(tree, start):
    visited = [False] * (v+1)
    q = deque([start])
    visited[start] = True
    while q:
        parent = q.popleft()
        print(parent, end=' ')
        for child in range(1, v+1):
            if not visited[child] and tree[parent][child]:
                q.append(child)
                visited[child] = True


if __name__ == '__main__':  # 음 그냥 깔끔해서 써봄.

    v, e, start = map(int, input().split())
    tree = list([0]*(v+1) for _ in range(v+1))
    visited = [False] * (v+1)

    # 트리 만들기
    for _ in range(e):
        v1, v2 = map(int, input().split())
        tree[v1][v2] = 1
        tree[v2][v1] = 1

    DFS(tree, start)
    print()
    BFS(tree, start)


def dfs(sheeps, wolves):
    global answer, visited, edges_, info_
    # [1] 늑대가 양보다 많을 때
    if sheeps <= wolves:
        return
    # [2] 탐색: 아직 미방문한 다음 노드
    for parent, child in edges_:
        if visited[parent] and not visited[child]:
            visited[child] = 1
            dfs(sheeps + (not info_[child]), wolves + info_[child])
            visited[child] = 0
    # [3] 양 최대값 갱신
    answer = max(answer, sheeps)


def solution(info, edges):
    global answer, visited, edges_, info_
    answer, visited = 0, [0] * len(info)
    visited[0] = 1
    edges_, info_ = edges, info 

    dfs(1, 0)

    return answer
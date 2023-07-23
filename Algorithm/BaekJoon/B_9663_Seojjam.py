# ////////////// 주연님 코드 보고 공부했습니다. //////////////

# < backtracking 진행절차 >

# ① 상태공간트리의 깊이우선검색(DFS)을 실시

# ② 각 노드가 유망(promising)한지 점검

# ③ 유망하지 않은 노드들은 더 이상 검색하지 않고 그 노드의 부모노드로 돌아가서 검색을 계속(pruning),\
#   유망한 노드들은 그 노드의 자식노드를 검색


def DFS(i):
    global nqueen
    if i == N:          # i가 N까지 오면 res +1
        nqueen += 1
    else:               # i가 N까지 올 동안 유망한지 계속 검사
        for j in range(1, N + 1):
            arr[i] = j              # arr에 어디 queen을 뒀는지 저장
            if promising(arr, i):   # 유망한지 검사 후 양호하면
                DFS(i + 1)          # 다음 행 검사


def promising(arr, i):
    for x in range(i):  # queen의 공격범위 안에 들면 return
        if arr[i] == arr[x] or abs(arr[i] - arr[x]) == i - x:
            return
    return True         # queen의 공격범위 밖에면 True


N = int(input())    # 체스판의 크기
arr = [0] * N       # 각 행마다 어느 열에 queen을 뒀는지 list
nqueen = 0             # N-Queen의 개수

DFS(0)
print(nqueen)
import sys
sys.stdin = open("sample_input.txt")
# [1] DFS
# [2] 유망한지

def DFS(i):
    global temp_sum
    global min_sum

    if i == N:                      # i가 N까지 도착하면 min_sum 최신화
        if temp_sum < min_sum:
            min_sum = temp_sum
    else:                           # i가 N까지 도착 전이면
        for j in range(N):          # j마다 유망한지 검사
            if promising(j):
                visited[i] = j
                temp_sum += arr[i][j]
                DFS(i + 1)          # 유망하면 계속 검사
                visited[i] = -1
                temp_sum -= arr[i][j]

def promising(j):
    if j in visited:            # 이미 방문 했으면 False
        return False
    elif temp_sum > min_sum:    # 여태 합이 min_sum 보다 높으면 False
        return False
    else:
        return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [-1] * N
    temp_sum = 0
    min_sum = 20
    DFS(0)
    print(f'#{tc} {min_sum}')
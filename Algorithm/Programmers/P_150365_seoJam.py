import sys
sys.setrecursionlimit(10**8)

# x,y: 현재 좌표 / temp: 문자열 / cnt: 남은 이동횟수
def dfs(x, y, temp, cnt):
    global answer
    dirs = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]

    # [1] 백트래킹: 남은 이동횟수 보다 이동거리가 더 크다면?
    if cnt < abs(x-R) + abs(y-C):
        return
    # [2] 종료조건: 이동이 끝나면?
    elif cnt == 0:
        if (x, y) == (R, C):
            answer = temp
        return
    # [3] 아직 이동할 수 있다면?
    for dx, dy, dir in dirs:
        if 0 < x+dx <= N and 0 < y+dy <= M and temp+dir < answer:
            dfs(x+dx, y+dy, temp+dir, cnt-1)


def solution(n, m, x, y, r, c, k):
    global R, C, N, M, answer
    R, C, N, M, answer = r, c, n, m, 'z'

    # [1] impossible 여부 확인
    distance = abs(x-r) + abs(y-c)
    if k < distance or (k - distance) % 2:
        return "impossible"
    # [2] dfs
    dfs(x, y, '', k)

    return answer

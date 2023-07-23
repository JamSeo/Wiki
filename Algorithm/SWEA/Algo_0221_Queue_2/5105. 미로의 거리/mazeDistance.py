import sys
sys.stdin = open("sample_input.txt")


def boundry(i, j):  # 경계값 판단 함수
    if i < 0 or j < 0 or i >= N or j >= N:
        return
    return True


# 12시부터 시계방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = []

    # 미로 받고, 출발점 찾기
    for i in range(N):
        maze.append(list(input()))  # str 값으로 받기
        if '2' in maze[i]:
            start_i, start_j = i, maze[i].index('2')

    q = [(start_i, start_j)]
    maze[start_i][start_j] = 0      # int형으로 0 저장
    find3 = 0                       # find3: 최종 출력값

    while q:
        i, j = q.pop(0)
        for k in range(4):
            new_i, new_j = i + di[k], j +dj[k]

            if not boundry(new_i, new_j):           # 미로 밖이야?
                continue

            elif maze[new_i][new_j] == '3':         # '3' 만났어?
                find3 = maze[i][j]                  # 바로 전 좌표값 저장
                break

            elif maze[new_i][new_j] == '0':         # '0' 만났어?
                maze[new_i][new_j] = maze[i][j] + 1 # '0'위에 int형 숫자를 1 더해서 미로에 저장
                q.append((new_i, new_j))

        if find3: break                          # '3' 찾았구나~ while문에서 나가!

    print(f'#{tc} {find3}')
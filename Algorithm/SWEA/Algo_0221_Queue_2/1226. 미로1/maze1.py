import sys
sys.stdin = open("input.txt")

# 12시부터 시계방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for _ in range(1, 11):
    tc = input()
    maze = []

    # 미로 받고, 출발점 찾기
    for i in range(16):
        maze.append(list(map(int, input())))
        if 2 in maze[i]:
            start_i, start_j = i, maze[i].index(2)

    q = [(start_i, start_j)]
    find3 = 0

    while q:
        i, j = q.pop(0)
        for k in range(4):
            new_i, new_j = i + di[k], j +dj[k]
            # 3 만났어?
            if maze[new_i][new_j] == 3:
                find3 = 1
                break
            # 0 만났어?
            elif not maze[new_i][new_j]:
                maze[new_i][new_j] = 1
                q.append((new_i, new_j))
        # 3 찾았구나~ 나가!
        if find3: break

    print(f'#{tc} {find3}')
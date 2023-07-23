import sys
sys.stdin = open("sample_input.txt")


DIRECTIONS = [
    (-1, 0), (0, -1), (1, 0), (0, 1)
]

def find(maze, now):
    for idx in range(4):
        direction = DIRECTIONS[idx]

        next_point = now[0] + direction[1], now[1] + direction[0]
        # 다음에 갈 곳이 3이면 도착이다!
        if maze[next_point[0]][next_point[1]] == 3:
            return 1
        # 갈곳이 열려있다!
        elif maze[next_point[0]][next_point[1]] == 0:
            maze[next_point[0]][next_point[1]] = 1
            # 막다른 길이라면?
            if not find(maze, next_point):
                # 돌아오자
                maze[next_point[0]][next_point[1]] = 0
            # 앞서 호출한 재귀함수가 성공했을 때
            else:
                return 1
    # 4방을 확인했지만 0이 없다면?
    return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # start
    start = None
    # 범위 판별이 귀찮으니 1을 넣어주자
    maze = [[1 for _ in range(N + 2)]]
    for i in range(N):
        maze_row = [1,]
        maze_row.extend(list(map(int, input())))
        maze_row.append(1)
        if 2 in maze_row:
            start = (i + 1, maze_row.index(2))
        maze.append(maze_row)
    maze.append([1 for _ in range(N + 2)])

    res = find(maze, start)
    print(f'#{tc} {res}')




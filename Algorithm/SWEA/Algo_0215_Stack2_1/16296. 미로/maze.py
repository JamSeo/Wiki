import sys
sys.stdin = open("sample_input.txt")

def boundry(i, j):  # 경계 체크
    if 0 <= i < N and 0 <= j < N:
        return True  # 경계 안
    return False  # 경계 밖


# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기
    maze = [list(map(int,input())) for _ in range(N)]  # 미로 형상

    # 출발점 구하기: start_i, start_j
    start_i = start_j = 0
    for i in range(N):
        if 2 in maze[i]:
            start_i, start_j = i, maze[i].index(2)
            break

    visited = [(start_i, start_j)]  # 시작점 스택에 추가
    res = 0  # 최종 출력값

    while visited:  # 반복범위 : 스택이 빌 때까지
        i, j = visited.pop()
        maze[i][j] = 1  # 방문처리
        print(i, j)

        for k in range(4):
            new_i, new_j = i + di[k], j + dj[k]

            # 경계 밖이면 넘어가
            if not boundry(new_i, new_j): continue

            # 주변에 '3'을 발견하면 1 반환
            elif maze[new_i][new_j] == 3:
                res = 1
                break

            # 주변에 '0'이 있으면
            elif not maze[new_i][new_j]:
                # 스택에 좌표 추가
                visited.append((new_i, new_j))

        # for문 종료되면 반복문 다시 진행
        else: continue
        
        # 주변에 '3'을 발견하면 while문 바로 탈출
        break

    print(f'#{tc} {res}')

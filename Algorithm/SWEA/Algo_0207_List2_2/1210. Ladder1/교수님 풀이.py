import sys
sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    for idx in range(100):  # 사다리 값이 2인 idx를 j에 저장
        if ladder[99][idx] == 2:
            x = idx
    y = 99

    # 좌우상
    dx = [-1, 1, 0]
    dy = [0, 0, -1]

    # 꼭대기에 도착할 때 까지 (y == 0일 때 까지)
    while y != 0:
        for dir_idx in range(3):  # 델타 검색
            new_x = x + dx[dir_idx]
            new_y = y + dy[dir_idx]

            if (0 <= new_x < 100 and 0 <= new_y < 100) \
                and ladder[new_y][new_x] == 1:
                ladder[y][x] = 0  # 온길을 0으로 처리해서 못돌아가게 조치
                x = new_x
                y = new_y

    print(f'#{tc} {x}')
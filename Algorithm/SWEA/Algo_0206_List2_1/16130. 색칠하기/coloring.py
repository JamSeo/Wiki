import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트케이스: 3

for tc in range(1, T+1):

    arr = []  # 10 x 10 격자 만들기
    for _ in range(10):
        arr.append(list([0] * 10))

    N = int(input())  # 칠할 영역의 개수 N ( 2 ≤ N ≤ 30 )

    for _ in range(N):
				# r1, c1: int -- 왼쪽모서리 좌표
				# r2, c2: int -- 오른쪽모서리
				# color: int -- 색상 (1: red / 2: blue)
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):  # 격자 내에 해당 영역 이쁘게 색칠하기☆
            for c in range(c1, c2+1):

                arr[r][c] += color

    # purple: int -- 보라색 칸 수 (3: purple)
    purple = 0
    for i in range(10):
        for j in range(10):

            if arr[i][j] == 3:  # if 보라색(값: 3)이면, purple += 1
                purple += 1

    print(f"#{tc} {purple}")

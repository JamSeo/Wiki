import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    tri = []  # tri: 2차원 [] -- 파스칼의 삼각형
    
    # [1]로 된 삼각형 만들기
    for i in range(N + 1):
        tri.append([1] * (i + 1))

    # 중간 값 계산
    for i in range(2, N + 1): # 다음 줄 왼쪽 끝
        for j in range(1, i):
            tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]

    for i in range(N):
        print(*tri[i])
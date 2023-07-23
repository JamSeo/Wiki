import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())

    # 사다리 : 양쪽에 0 하나씩 붙임
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    
    # result : {} -- 결과값 저장 / key: 시작점, value: 이동거리
    result = dict()
    start = int()

    for j in range(101):
        i = cnt = 0
        if ladder[0][j] == 1:  # [] 첫 줄에 1인 곳에서 while문 시작
            start = j - 1  # 해당 j는 start에 저장

            while i != 100:  # i가 100에 도달할 때 까지

                # 왼쪽에 1있는 경우
                if ladder[i][j - 1]:
                    while ladder[i][j - 1]:
                        j -= 1
                        cnt += 1
                    else:
                        i += 1
                        cnt += 1

                # 오른쪽에 1있는 경우
                elif ladder[i][j + 1]:
                    while ladder[i][j + 1]:
                        j += 1
                        cnt += 1
                    else:
                        i += 1
                        cnt += 1

                # 양쪽에 아무것도 없는 경우
                else:
                    i += 1
                    cnt += 1
            else:
                result[start] = cnt

    for j in result:
        if result[j] == min(result.values()):
            print(f'#{tc} {j}')


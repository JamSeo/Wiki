import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    # N : int -- 글자판의 가로세로 크기 (10 ≤ N ≤ 100)
    # M : int -- 회문의 길이 (5 ≤ M ≤ N)
    # arr : [] -- NxN 크기의 글자판
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''

    # for문 : 가로가 회문이면 ans에 저장후 출력
    # else문 : 세로가 회문이면 ans에 저장 후 출력
    for i in range(N):
        arr_1 = ''
        for j in range(N - M + 1):
            arr_1 = ''.join(arr[i][j : j + M])

        if arr_1 == arr_1[::-1]:
            ans = arr_1
            break

    else:
        for j in range(N):
            for i in range(N - M + 1):
                arr_2 = ''
                for m in range(M):
                    arr_2 += arr[i+m][j]
                arr_2 = ''.join(arr_2)

                if arr_2 == arr_2[::-1]:
                    ans = arr_2
                    break
            else:
                continue
            break

    print(f'#{tc} {ans}')

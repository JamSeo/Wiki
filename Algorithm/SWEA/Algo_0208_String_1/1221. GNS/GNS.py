import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())

for tc in range(1, T+1):

    # tc : str -- # 테스트 케이스
    # N : int -- 문자열 길이
    # arr : [] -- 입력 문자열
    tc, N = input().split()
    arr = list(input().split())
    N = int(N)

    # alp : [] -- 0 ~ 9까지 문자열
    alp = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # rlst : [] -- 출력할 리스트
    rslt = [tc]

    for num in alp:
        for i in range(N):
            if arr[i] == num:
                rslt. append(arr[i])

    print(*rslt)

import sys
sys.stdin = open("input1.txt")

T = int(input())  # 테스트 케이스 : 3

for tc in range(1, T+1):
    N = int(input())  # 수열의 길이 : 10
    sequence = list(map(int, input()))  # 수열 []
    ans = cnt = 0

    for i in range(N):
        if sequence[i] == 0:  # else 수열에서 0이 나오면,
            cnt = 0  # cnt = 0으로 리셋

        else:  # if 수열에서 1이 나오면,
            cnt += 1  # cnt +1
            if ans < cnt:
                ans = cnt

    print("#{} {}".format(tc, ans))


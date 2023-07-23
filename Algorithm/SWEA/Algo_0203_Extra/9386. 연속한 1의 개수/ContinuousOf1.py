import sys
sys.stdin = open("input1.txt")

T = int(input())  # 테스트 케이스 : 3

for tc in range(1, T+1):
    N = int(input())  # 수열의 길이 : 10
    sequence = list(map(int, input()))  # 수열 []
    print(sequence)

    cnt = 0  # 1이 연속된 개수
    cnt_lst = []  # cnt 저장 []

    for i in sequence:
        if i == 1:  # if 수열에서 1이 나오면,
            cnt += 1  # cnt +1
            cnt_lst.append(cnt)  # cnt 값 []에 저장

        else:  # else 수열에서 0이 나오면,
            cnt = 0 # cnt = 0으로 리셋

    rslt = max(cnt_lst)  # 1이 연속된 개수의 최댓값 저장
    print("#{} {}".format(tc, rslt))


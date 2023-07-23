import sys
sys.stdin = open("sample_input.txt")


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N: 화덕의 크기, M: 피자 개수
    C = list(map(int, input().split())) # C: 피자에 뿌려진 치즈의 양
    pot = []                            # pot: 화로

    pidx = 0
    for _ in range(N):
        pidx += 1
        pot.append([C.pop(0), pidx])    # 화로 크기(N) 만큼 [치즈양, 피자번호] 넣어줌

    while len(pot) != 1:    # 반복범위 : 피자가 하나 남을 때 까지
        pot[0][0] //= 2     # 화로 속에 돌면서 치즈양 반으로 줄임

        if pot[0][0] == 0:  # 치즈양이 0이 되고
            if C:           # 남은 피자가 있으면
                pidx += 1   # 다음 피자 구워
                pot.append([C.pop(0), pidx])
            pot.pop(0)      # 해당 피자 제거
        else:
            pot.append(pot.pop(0))  # 화로 안의 첫 피자 맨 뒤로 보내기

    print(f'#{tc} {pot[0][1]}')
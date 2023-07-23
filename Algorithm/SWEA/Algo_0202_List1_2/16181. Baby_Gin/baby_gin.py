import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트케이스 : 9

for tc in range(1, T+1):

    num = int(input())  # 카드숫자 입력
    c = [0] * 12  # 각 자리 수를 추출하여 개수를 누적할 리스트

    for i in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0  # tri: triplet 수  # run: run 수

    while i < 10:
        if c[i] >= 3:  # triplet 조사 후 데이터 삭제
            c[i] -= 3
            tri += 1
            continue

        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:  # run 조사 후 데이터 삭제
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i+=1

    if run + tri == 2: result = 1  # if baby-gin이면, 결과 : 1
    else: result = 0  # 아니면, 결과 : 0

    print("#{} {}".format(tc, result))
import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스 : 10

for tc in range(1, T+1):

    N = int(input())
    divs = [2, 3, 5, 7, 11]
    cnts = [0] * len(divs)  # a,b,c,d,e 저장[]

    for i in range(len(divs)):
        while N % divs[i] == 0:  # while divs[i]로 나누어 떨어질 때 까지
            N //= divs[i]  # N을 divs[i]로 나누고
            cnts[i] += 1  # cnt 1씩 더해짐

    print(f"#{tc}", *cnts)
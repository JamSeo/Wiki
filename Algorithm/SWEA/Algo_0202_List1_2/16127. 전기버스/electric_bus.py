import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트케이스 : 3

for tc in range(1, T+1):

    # K : 한번 충전하고 이동할 수 있는 값
    # N : 종점
    # M : 충전소 수
    K, N, M = map(int, input().split())

    # stops : 충전소 위치 리스트
    stops = list(map(int, input().split()))
    
    here = 0  # 현위치
    charge = 0  # 충전 수

    while here + K < N:  # while 종점까지
        
        for move in range(K, 0, -1): # 이동거리(move)는 K부터 0 순으로 대입

            if (here + move) in stops:  # if 현위치(here)에서 이동거리(move) 안에 충전소가 있으면
                here += move  # 해당 충전소를 현위치로 저장
                charge += 1  # 충전수 +1
                break
            
        else:  # else 충전소가 없다면
            charge = 0  # 충전 수 : 0
            break
        
    print("#{} {}".format(tc, charge))
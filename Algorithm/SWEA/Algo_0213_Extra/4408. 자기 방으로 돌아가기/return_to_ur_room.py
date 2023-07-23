import sys
sys.stdin = open("sample_input.txt")

# [1] 복도 리스트 만들기: [0] * 200
# [2] start&end 입력받아서 리스트에 넣기
# [3] 리스트 최댓값 출력

T = int(input())  # T : 테스트케이스 수

for tc in range(1, T + 1):
    N = int(input())        # N : 돌아가야 할 학생들의 수
    corridor = [0] * 200    # corridor : 복도 리스트

    for _ in range(N):
        start, end = map(int, input().split())
        
        if start > end:     # 반례 : 방번호가 큰방에서 작은방으로 이동하는 경우
            start, end = end, start

        for idx in range((start-1)//2, (end-1)//2 + 1):
            corridor[idx] += 1

    time = max(corridor)
    print(f'#{tc} {time}')





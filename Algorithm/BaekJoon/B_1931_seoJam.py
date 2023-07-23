# 최초에 회의 시작시간으로 정렬했다가 몰매 맞았습니다.
# 구글링을 통해 회의 종료시간 정렬이 더 빠르다는 것을 알게 되었고
# 구현에 성공하였습니다.
import sys
input = sys.stdin.readline

N = int(input())  # 회의 수
schedule = []     # 회의 리스트
for _ in range(N):
    start, end = map(int, input().split())
    schedule.append([start, end])
# [1] 회의 종료시간 순으로 sort(같으면 시작시간 역순)
schedule.sort(key=lambda x: (x[1], x[0]))
# [2] 종료시간이 가장 빠른 회의부터 탐색 시작
cnt = 1
now_end = schedule[0][1]
for next in range(1, N):
    if now_end <= schedule[next][0]:
        now_end = schedule[next][1]
        cnt += 1
print(cnt)
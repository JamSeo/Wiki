import sys
sys.stdin = open("sample_input.txt")

# (방번호 - 1) // 2 : 복도번호
# [1] 시작복도번호 ~ 끝복도번호 : 누적 cnts 표시
# [2] 최댓값 찾기

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    corridor = [0] * 200  # 복도 리스트

    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:  # 방번호 거꾸로 이동할 경우
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2 + 1):
            corridor[i] += 1

    ans = max(corridor)
    print(f'#{tc} {ans}')
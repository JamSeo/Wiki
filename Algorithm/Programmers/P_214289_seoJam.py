def solution(temperature, t1, t2, a, b, onboard):
    # 실외온도를 0, t1을 최소온도, t2를 최대온도로 저장.
    t1, t2 = t1 - temperature, t2 - temperature
    if t2 < 0:
        t1, t2 = -t2, -t1

    # dp: 행(온도), 열(시간; 분)
    dp = [[1e5 for _ in range(len(onboard))] for _ in range(51)]
    # 첫 승객 탑승시간
    start_j = onboard.index(True) if True in onboard else 0
    # dp 시작값 저장
    dp[t1][start_j] = a * t1

    # dp 채우기
    for j in range(start_j + 1, len(onboard)):
        for i in range(50):
            # 승객이 탔다?
            if onboard[j]:
                if i < t1:
                    continue
                dp[i][j] = min(dp[i-1][j-1]+a, dp[i][j-1]+b, dp[i+1][j-1])
            # 승객이 없다?
            else:
                if i == 0:
                    dp[i][j] = min(dp[i][j-1], dp[i+1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j-1]+a, dp[i][j-1]+b, dp[i+1][j-1])

    answer = 1e9
    for ddp in dp:
        if answer > ddp[-1]:
            answer = ddp[-1]

    return answer

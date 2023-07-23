def solution(alp, cop, problems):
    # [1] 알고력, 코딩력 최댓값 구하기
    max_alp = max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])

    # [2] 처음의 알고력, 코딩력이 최댓값 보다 크거나 같으면? 0 반환
    if alp >= max_alp and cop >= max_cop:
        return 0
    else:  # 둘 중 하나라도 최댓값 보다 크거나 같을수도..
        alp = min(alp, max_alp)
        cop = min(cop, max_cop)

    # [3] DP 만들기
    max_alp -= alp
    max_cop -= cop
    dp = list([al+co for co in range(max_cop+1)] for al in range(max_alp+1))
    dp[0][0] = 0  # 출발점

    # [4] 문제 풀기
    for i in range(max_alp+1):
        for j in range(max_cop+1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 문제 풀 수 있다면?
                if i >= alp_req-alp and j >= cop_req-cop:
                    # 멍청하게 아래처럼 조건 4개씩 달았다가.. 지현님꺼 보고 수정했습니다.
                    ni, nj = min(i + alp_rwd, max_alp), min(j + cop_rwd, max_cop)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + cost)

                    # # (1) 알고력, 코딩력 둘 다 max 값을 넘겼을 때
                    # if i + alp_rwd > max_alp and j + cop_rwd > max_cop:
                    #     dp[max_alp][max_cop] = min(dp[max_alp][max_cop], dp[i][j] + cost)
                    # # (2)알고력만 max 값을 넘겼을 때
                    # elif i+alp_rwd > max_alp:
                    #     dp[max_alp][j+cop_rwd] = min(dp[max_alp][j+cop_rwd], dp[i][j]+cost)
                    # # (3) 코딩력만 max 값을 넘겼을 때
                    # elif j+cop_rwd > max_cop:
                    #     dp[i+alp_rwd][max_cop] = min(dp[i+alp_rwd][max_cop], dp[i][j]+cost)
                    # # (4) 둘 다 max 값보다 작을 때
                    # else:
                    #     dp[i+alp_rwd][j+cop_rwd] = min(dp[i+alp_rwd][j+cop_rwd], dp[i][j]+cost)
    answer = dp[max_alp][max_cop]
    return answer
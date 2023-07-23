import sys
input = sys.stdin.readline

def who_is_my_team(idx, N):  # DFS()
    global cnt
    global answer

    # [2] 팀이 정해지면 Sij, Sji 합 구하기
    if cnt == N//2:
        teamTrue, teamFalse = 0, 0
        for i in range(N):
            for j in range(N):
                # 둘다 True team이야?
                if visited[i] and visited[j]:
                    teamTrue += S[i][j]
                # 둘다 False team이야?
                elif not visited[i] and not visited[j]:
                    teamFalse += S[i][j]

        # [3] 팀별 능력치 차이 구하고 최솟값 출력
        answer = min(answer, abs(teamTrue - teamFalse))
        return

    # [1] True/False 팀으로 나눠주기
    for i in range(idx, N):
        if visited[i] == False:
            visited[i] = True
            cnt += 1
            who_is_my_team(i+1, N)
            visited[i] = False
            cnt -= 1


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
cnt, answer = 0, 100
who_is_my_team(0, N)
print(answer)
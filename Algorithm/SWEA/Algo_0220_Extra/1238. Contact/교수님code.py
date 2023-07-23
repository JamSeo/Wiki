import sys
sys.stdin = open("input.txt")

def bfs(s):
    # [0] q, v, 필요한 flag 생성
    q = []
    v = [0] * 101
    ans = s
    # [1] q에 초기데이터(들) 삽입, v표시
    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)    # [2] q에서 하나 꺼냄 + 필요시 정담꺼냄
        if v[ans] < v[c] or v[ans] == v[c] and ans < c:
            ans = c

        # [3] 4/8 연결방향 등 반복처리
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return ans


for tc in range(1, 11):
    E, S = map(int, input().split())
    lst = list(map(int, input().split()))
    # [1] 인접리스트에 연결 저장
    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        s, e = lst[i], lst[i+1]
        adj[s].append(e)

    ans = bfs(s)
    print(f'#{tc} {ans}')
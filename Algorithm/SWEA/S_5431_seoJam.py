T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    who_submit = list(map(int, input().split()))
    ans = []

    for i in range(1, N+1):
        if i not in who_submit:
            ans.append(i)

    print(f'#{tc}', *ans)

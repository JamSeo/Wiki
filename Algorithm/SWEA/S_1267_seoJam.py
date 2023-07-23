for tc in range(1, 11):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = list([] for _ in range(V + 1))
    stack = []
    ans = []

    # [1] 트리 구성하기 (선행과제를 요소로 가지는 트리)
    for idx in range(E):
        before, after = temp[idx * 2], temp[idx * 2 + 1]
        tree[after].append(before)

    # [2] 선행 과제가 없는 업무 찾기(==빈 리스트; 가장 먼저 처리할 업무)
    for start in range(1, V+1):
        if not tree[start]:
            stack.append(start)

    # [3] 업무 순서 DFS
    while stack:
        now_work = stack.pop()
        ans.append(now_work)    # ans에 업무 순서 저장

        for next_work in range(1, V+1):         # now_work가 선행 과제인 업무 찾기
            if now_work in tree[next_work]:
                tree[next_work].remove(now_work)  # 찾으면 삭제

                if not tree[next_work]:         # 남은 선행과제가 더 없다면?
                    stack.append(next_work)       # 다음 과제하러 가기

    print(f'#{tc}', *ans)
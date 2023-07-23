import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N: 노드의 개수, M: 리프 노드의 개수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    # tree 만들기
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    # 빈칸에 값 채워주기
    for i in range(N-1, 0, -1):
        if not tree[i]:
            if i * 2 + 1 > N:
                tree[i] = tree[i * 2]
            else:
                tree[i] = tree[i * 2] + tree[i * 2 + 1]
        # idx = L에 값 채워줬으면 탈출
        if i == L:
            break

    print(f'#{tc} {tree[L]}')

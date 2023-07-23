import sys
sys.stdin = open("sample_input.txt")

for tc in range(int(input())):
    N, Q = map(int, input().split())
    box = [0 for _ in range(N)]

    for i in range(Q):
        L, R = map(int, input().split())

        for n in range(L-1, R):
            box[n] = i + 1

    print(f'#{tc+1}', *box)
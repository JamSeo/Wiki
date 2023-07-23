def making(idx):
    global number
    if idx <= N:
        making(idx * 2)
        tree[idx] = number
        number += 1
        making(idx * 2 + 1)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    number = 1
    making(1)
    print(f'#{t} {tree[1]} {tree[N//2]}')
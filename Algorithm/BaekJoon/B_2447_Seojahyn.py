import sys
sys.stdin = open("input.txt")

def star(N):
    n = N // 3
    if n == 1:
        return ['***','* *','***']

    arr = star(n)
    lst = []

    for i in arr:
        lst.append(i * 3)

    for i in arr:
        lst.append(i + ' ' * n + i)

    for i in arr:
        lst.append(i * 3)

    return lst

N = int(input())
print('\n'.join(star(N)))

# //////////////////////////////////
# 절망적이네요. 구글링 해버렸습니다.

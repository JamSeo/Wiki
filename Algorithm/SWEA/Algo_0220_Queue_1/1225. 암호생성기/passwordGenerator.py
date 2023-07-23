import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))

    i = 0
    while True:
        i += 1                      # i는 1씩 증가
        if i > 5: i %= 5

        data[0] -= i                # i만큼 빼고
        data.append(data.pop(0))    # 맨뒤로 보내기

        if data[-1] <= 0:           # 값이 0보다 작으면?
            data[-1] = 0            # 0으로 저장 후 break
            break

    print(f'#{tc}', *data)

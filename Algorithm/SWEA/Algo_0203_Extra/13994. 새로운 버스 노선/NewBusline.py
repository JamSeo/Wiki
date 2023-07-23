import sys
sys.stdin = open("sample_in.txt")

T = int(input())  # 테스트케이스: 1

for tc in range(1, T+1):
    N = int(input())  # 노선 수: 3
    lst = [0] * 1001  # 1~1000번까지 정류장

    for _ in range(N):
        type, A, B = map(int, input().split())

        if type == 1:
            for i in range(A, B + 1):
                lst[i] += 1

        elif type == 2:
            if not A % 2:
                for i in range(A, B+1):
                    if not i % 2:
                        lst[i] += 1
            else:
                for i in range(A, B+1):
                    if i % 2:
                        lst[i] += 1

        else:
            if not A % 2:
                for i in range(A, B+1):
                    if not i % 4:
                        lst[i] += 1

            else:
                for i in range(A, B+1):
                    if i % 10 and not i % 3:
                        lst[i] += 1

    rslt = max(lst)
    print('#{} {}'.format(tc, rslt))



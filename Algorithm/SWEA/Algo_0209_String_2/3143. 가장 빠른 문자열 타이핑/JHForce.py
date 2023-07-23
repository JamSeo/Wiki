import sys
sys.stdin = open("sample_input.txt")

def JHForce(p, t):
    N = len(t)  # target의 글자수
    M = len(p)  # pattern의 글자수
    cnt = i = j= 0  # i: target의 idx / j: pattern의 idx

    while i < N:  # 매칭 돌립니다~!~!

        # 철자 일치 O
        if t[i] == p[j]:
            pass

        # 철자 일치 X
        else:
            # target의 철자가 pattern 안에 O
            if t[i] in p:
                # 해당 철자를 pattern에서 찾고 그 idx만큼 i값 이동
                for idx in range(M):
                    if p[idx] == t[i]:
                        i = i - j + idx -1
                        j = -1

            # target의 철자가 pattern 안에 X
            else:
                j = -1

        # 매칭 성공 O
        if j == M - 1:
            cnt += 1
            j = -1

        i += 1
        j += 1

    return cnt


T = int(input())  # 테스트케이스: 2

for tc in range(1, T+1):
    A, B = input().split()

    a = len(A)
    b = len(B)
    n = JHForce(B, A)
    ans = a - n * (b - 1)

    print(f'#{tc} {ans}')
import sys
sys.stdin = open("sample_input.txt")

def binary_search(l, r, key):
    cnt = 0
    while l <= r:
        c= int((l+r) // 2)

        if c == key:
            cnt += 1
            return cnt

        elif c < key:
            cnt += 1
            l = c

        else:
            cnt += 1
            r = c

T = int(input())
for tc in range(1, T+1):
    # P : int -- 책의 전체 쪽수
    # A : int -- A가 찾을 쪽 번호
    # B : int -- B가 찾을 쪽 번호
    P, A, B = map(int, input().split())
    ca = binary_search(1, P, A)
    cb = binary_search(1, P, B)
    print(ca, cb)

    if ca < cb:
        print(f'#{tc} A')
    elif ca > cb:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
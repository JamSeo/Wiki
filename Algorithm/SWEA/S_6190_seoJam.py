T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    temp = []
    ans = -1

    for i in range(N-1):
        for j in range(i + 1, N):
            temp.append(A[i] * A[j])

    temp.sort(reverse=True)             # temp 내림차순 정렬
    temp = list(map(str, temp))         # int형에서 str형으로 변환  # ['28']

    for num in temp:
        num = list(num)                 # 자릿수 별로 쪼개서 list로 저장 ['2', '8']

        for i in range(len(num) - 1):   # 단조 증가가 아니면 break
            if num[i] > num[i + 1]:
                break
        else:                           # 단조 증가면 ans에 저장 후 출력
            ans = ''.join(num)
            break

    print(f'#{tc} {ans}')
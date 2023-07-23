import sys
sys.stdin = open("sample_input.txt")

def special_sort(a, start, N):

    while start < N:  # while문 범위 : start == N이 될 때 까지

        maxIdx = start  # 최댓값 찾아서 맨 앞자리랑 자리 교환하기
        for i in range(start, N):
            if a[maxIdx] <= a[i]:
                maxIdx = i
        a[maxIdx], a[start] = a[start], a[maxIdx]

        start += 1  # 맨앞자리 +1

        minIdx = start  # 최솟값 찾아서 맨 앞자리랑 자리 교환하기
        for j in range(start+1, N):
            if a[minIdx] >= a[j]:
                minIdx = j
        a[minIdx], a[start] = a[start], a[minIdx]

        start += 1  # 맨 앞자리 +1

    return a


T = int(input())  # 테스트케이스: 3

for tc in range(1, T+1):

    N = int(input())  # N: 정수의 개수
    lst = list(map(int, input().split()))
    special_sort(lst, 0, len(lst))

    print(f'#{tc}', *lst[:10])  # 리스트 요소 10개만 출력
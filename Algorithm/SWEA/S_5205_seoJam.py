def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)

def partition(arr, l, r):
    pivot = arr[l]
    i, j = l+1, r
    while i <= j:
        while (i<=j and arr[i]<=pivot): i += 1
        while (i<=j and arr[j]>=pivot): j -= 1
        if i <= j:  # 해당 조건 빼먹어서 애먹음;;
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


if __name__ == '__main__':

    for tc in range(1, int(input()) + 1):
        N = int(input())
        A = list(map(int, input().split()))

        quickSort(A, 0, N-1)

        print('#{} {}'.format(tc, A[N//2]))

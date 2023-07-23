# 시간초과 계속 떠서 구글링 하니까 append 쓰면 안된대서 결국 복잡시럽게 구현됨.

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # 여기서 l,r을 deque로 구현하면 더 빠를듯!
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    global cnt
    len_l, len_r = len(left), len(right)
    res = [0] * (len_l + len_r)
    i = l_idx = r_idx = 0

    while l_idx < len_l and r_idx < len_r:
        if left[l_idx] <= right[r_idx]:
            res[i] = left[l_idx]
            l_idx += 1
        else:
            res[i] = right[r_idx]
            r_idx += 1
        i += 1

    if l_idx < len_l:
        cnt += 1
        res[i:] = left[l_idx:]
    if r_idx < len_r:
        res[i:] = right[r_idx:]

    return res


if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        n = int(input())
        arr = list(map(int, input().split()))
        cnt = 0

        arr = mergeSort(arr)

        print('#{} {} {}'.format(tc, arr[n//2], cnt))

def f(i, k, key):
    if i == k:  # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]   # 부분집합의 합

        if s == key:        # 합이 key와 같은 부분집합 출력
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
            print()
    else:
        bit[i] = 1      # 1을 넣을까
        f(i+1, k, key)
        bit[i] = 0      # 말까
        f(i+1, k, key)


A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 10
bit = [0] * N
f(0, N, key)
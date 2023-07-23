def f(i, k, s, t):
    # i 원소, k 집합크기, s 부분집합의 합, t 찾고자 하는 값
    global cnt

    if s > t: return    # 이미 부분집합의 합이 target보다 큰 경우: 더 진행 X
    elif s == t:        # 이미 부분집합의 합이 target과 같게된 경우: 나머지 고려할 필요 X
        cnt += 1
        return
    elif i == k: return  # 모든 원소를 고려한 경우
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 10
cnt = 0
bit = [0] * N
f(0, N, 0, key)
print(cnt)      # 합이 key인 부분집합의 수
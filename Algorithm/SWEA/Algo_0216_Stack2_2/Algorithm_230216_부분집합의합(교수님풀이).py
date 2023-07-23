arr = list(range(1, 11))
N = 10  # len(arr)

# arr = 원소 후보들
# idx = idx번째 원소
# subset = 부분집합
# powerset이라는 함수의 역할은 idx번째 원소를 부분집합에 포함시킬까 결정
# + 현재 부분집합이 답이 될 가능성이 남아있는지 판단
# + 현재 부분집합이 답인지 판단

def powerset(arr, idx, subset):
    # 현재 부분집합의 합과 남은 것들의 합을 더해도 답이 안됨
    if sum(subset) + sum(arr[idx:]) < 10:
        return
    # 현재 부분집합의 합이 답이 될 가능성 없음
    if sum(subset) > 10:
        return
    # 부분집합 다 만듬
    if idx == N:
        if sum(subset) == 10:
            print(subset)
            # print(True)
        return
    # 현재 원소 포함 (왼쪽)
    powerset(arr, idx + 1, subset + [arr[idx]])
    # 현재 원소 불포함 (오른쪽)
    powerset(arr, idx + 1, subset)

powerset(arr, 0, [])
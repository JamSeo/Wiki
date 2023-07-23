# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def boundry(i, j):  # 경계값 여부 함수
    if i<0 or j<0 or N<=i or N<=j:
        return False
    return True

def count_house(arr, i , j):  # 단지수 반환 함수
    cnt = 1
    arr[i][j] = '0'
    stack = [(i, j)]
    while stack:
        si, sj = stack.pop()
        for k in range(4):
            ni, nj = si+di[k], sj+dj[k]
            if boundry(ni, nj) and arr[ni][nj] == '1':
                cnt += 1
                arr[ni][nj] = '0'
                stack.append((ni, nj))
    return cnt


N = int(input())
arr = [list(input()) for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            ans.append(count_house(arr, i, j))

ans.sort()
n = len(ans)
print(n)
for idx in range(n):
    print(ans[idx])
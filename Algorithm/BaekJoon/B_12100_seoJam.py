# deepcopy() : 단순복제를 하는 copy()와 달리 별개의 복제된 버전 생성 ==> 원본에 서로 영향 X
# copy() : 1차원 리스트에서는 원본과 서로 영향을 미치지 않지만, 2차원 부터는 영향 O (복사본의 요소를 바꾸면 원본 요소도 바뀜)
from copy import deepcopy

# 입력된 방향의 끝에서 부터 숫자를 채워줄 예정
def shake(arr, n):
    if n == 0:    # Right
        for i in range(N):
            end = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][end] == 0:        # 끝점이 0이면 temp값 입력
                        arr[i][end] = temp
                    elif arr[i][end] == temp:   # 끝점이 같은 값이면 2곱하고, 끝점을 앞으로 한칸
                        arr[i][end] *= 2
                        end -= 1
                    else:                       # 끝점이 다른 값이면 끝점을 앞으로 한칸, temp값 입력
                        end -= 1
                        arr[i][end] = temp

    elif n == 1:  # Left
        for i in range(N):
            end = 0
            for j in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][end] == 0:
                        arr[i][end] = temp
                    elif arr[i][end] == temp:
                        arr[i][end] *= 2
                        end += 1
                    else:
                        end += 1
                        arr[i][end] = temp
    elif n == 2:  # Down
        for j in range(N):
            end = N-1
            for i in range(N-2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[end][j] == 0:
                        arr[end][j] = temp
                    elif arr[end][j] == temp:
                        arr[end][j] *= 2
                        end -= 1
                    else:
                        end -= 1
                        arr[end][j] = temp
    elif n == 3:  # Up
        for j in range(N):
            end = 0
            for i in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[end][j] == 0:
                        arr[end][j] = temp
                    elif arr[end][j] == temp:
                        arr[end][j] *= 2
                        end += 1
                    else:
                        end += 1
                        arr[end][j] = temp
    return arr


def DFS(arr, cnt):
    global ans
    if cnt == 5:        # DFS 5번 하면 최댓값 출력 후 끝
        for i in range(N):
            for j in range(N):
                ans = max(ans, arr[i][j])
        return
    for n in range(4):  # 4방향으로 흔들기
        temp_arr = shake(deepcopy(arr), n)  # deepcopy()
        DFS(temp_arr, cnt + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = cnt = 0
DFS(arr, 0)
print(ans)

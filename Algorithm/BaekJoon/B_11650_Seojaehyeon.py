N = int(input())  # 점의 개수
dot = []  # 점 좌표 []

for _ in range(N):  # 좌표 받아서 튜플()로 []에 추가
    (x, y) = tuple(map(int, input().split()))
    dot.append((x, y))

dot.sort(key = lambda x:(x[0], x[1]))  # x로 먼저 정렬, x가 같으면 y로 정렬  # 새로 알게된 방법

for x, y in dot:
    print(x, y)


# # # # # # # # # Bubble Sort # # # # # # # #

# for i in range(N-1, 0, -1):  # i : 4, 3, 2, 1

#     for j in range(0, i):
#         if dot[j][0] > dot[j+1][0]:  # 먼저 x 기준 정렬
#             dot[j], dot[j+1] = dot[j+1], dot[j]

#         elif dot[j][0] == dot[j+1][0]:  # x가 같다면 y 기준 정렬
#             for _ in range(2):
#                 if dot[j][1] > dot[j+1][1]:
#                     dot[j], dot[j+1] = dot[j+1], dot[j]

# for x, y in dot:
#     print(x, y)
# # # # # # # # # RuntimeError # # # # # # # # #

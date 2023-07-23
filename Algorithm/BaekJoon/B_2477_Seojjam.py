import sys
input = sys.stdin.readline

# K: int -- 1m2의 넓이에 자라는 참외의 개수
# bndry : [] -- 참외밭 전체 경계 리스트
# wid, len: [] -- 참외밭의 가로, 세로 경계 리스트
K = int(input())
bndry = []
wid, len = [], []

for _ in range(6):
    # dir, dis : int -- 이동방향, 이동거리
    dir, dis = map(int, input().split())

    bndry.append(dis)
    if dir == 1 or dir == 2:
        wid.append(dis)
    elif dir == 3 or dir == 4:
        len.append(dis)
# print(bndry)  # [50, 160, 30, 60, 20, 100]
# print(wid)  # [160, 60, 100]
# print(len)  # [50, 30, 20]


# 밭의 큰 넓이 : max(wid) x max(len)
max_wid = max(wid)
max_len = max(len)
area1 = max_wid * max_len  # 8000

# 빼줄 넓이 : bndry[max_wid의 idx - 3] x bndry[max_len의 idx - 3]
# cf. max_wid = 160 = bndry[1] 이니까 'bndry[1 - 3]'과
#       max_len = 50 = bndry[0] 이므로 'bndry[0 - 3]'을 곱해줌
area2 = 1
for i in range(6):
    if bndry[i] == max_wid or bndry[i] == max_len:
        area2 *= bndry[i - 3]  # 1200

# 마지막 참외의 개수 : K x (area1 - area2)
print(K * (area1 - area2))
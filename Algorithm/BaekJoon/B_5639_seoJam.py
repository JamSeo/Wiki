# 구글링 100%
# https://ku-hug.tistory.com/132 참조

# [1] for문으로 루트 노드(preorder[start])보다 커지면 오른쪽 노드!
#     왼쪽, 오른쪽 나뉘는 부분을 mid로 저장
#
# [2] 왼쪽 노드[s+1, mid-1], 오른쪽 노드[mid, e]로 나누기
#     -> 왼쪽 노드들만 확인(재귀) -> 가장 작은 트리까지! 루트 출력!
#     -> 다음 오른쪽 노드 확인(재귀)

import sys
sys.setrecursionlimit(10 ** 4)

# 후위순회 함수
def postorder(start, end):
    if start > end: return      # 함수 종료조건
    mid = end + 1               # 만약 모든 원소가 루트 노드보다 작은 경우 대비

    for i in range(start+1, end+1):
        if preorder[start] < preorder[i]:   # 기준(start)보다 값이 크면 break
            mid = i
            break

    postorder(start+1, mid-1)   # 왼쪽 트리 검색
    postorder(mid, end)         # 오른쪽 트리 검색
    print(preorder[start])      # 루트 노드 출력


# 전위순회 결과 입력받기
preorder = []
while True:
    try: preorder.append(int(input()))
    except EOFError: break

postorder(0, len(preorder)-1)
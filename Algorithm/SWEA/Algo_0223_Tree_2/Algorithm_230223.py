
# last = 0  # 힙에 추가된 총 노드들
# heap = [0] * 101  # 힙 공간 확보
#
# def enq(node):
#     global last
#     last += 1
#     heap[last] = node
#     child = last  # 마지막으로 추가된 위치
#     parent = child // 2  # 그 부모
#     # 부모와 반복적으로 비교해가며 위치를 조정해간다.
#     # parent의 idx의 가장 작은 값은 1
#     # 부모가 자식보다 작으면 교체하고, 커지면 그 다음은 할 필요 없음
#     while parent > 0 and heap[parent] < heap[child]:
#         # 둘 위치를 바꾼다
#         heap[parent], heap[child] = heap[child], heap[parent]
#         # 바뀌었으면 새 부모랑 비교할 준비
#         child = parent
#         parent = child // 2
#
# def deq():
#     global last
#     tmp = heap[1]
#     heap[1] = heap[last]
#     # 크기가 줄었으니 노드의 갯수를 조정
#     last -= 1
#     parent = 1
#     child = parent * 2
#
#     while child <= last:
#         # 만약 오른쪽이 더 크면, 왼쪽이 부모가 되었을 때 힙이 아니게 된다.
#         if child + 1 <= last and heap[child] < heap[child + 1]:
#             child += 1  # 대상을 오른쪽으로 바꾸자.
#         # 힙을 만족시키도록 값을 교환
#         if heap[child] > heap[parent]:
#             heap[parent], heap[child] = heap[child], heap[parent]
#             parent = child
#             child = parent * 2
#         # 아니면 반복중단
#         else:
#             break
#     return tmp

# ///////////////////////////////////////////////////////////////////

heap = [0]

def enq(node):
    heap.append(node)
    child = len(heap) - 1  # 마지막으로 추가된 위치
    parent = child // 2  # 그 부모
    # 부모와 반복적으로 비교해가며 위치를 조정해간다.
    # parent의 idx의 가장 작은 값은 1
    # 부모가 자식보다 작으면 교체하고, 커지면 그 다음은 할 필요 없음
    while parent > 0 and heap[parent] < heap[child]:
        # 둘 위치를 바꾼다
        heap[parent], heap[child] = heap[child], heap[parent]
        # 바뀌었으면 새 부모랑 비교할 준비
        child = parent
        parent = child // 2

def deq():
    tmp = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    parent = 1
    child = parent * 2
    while child < len(heap):
        if child + 1 < len(heap) and heap[child] < heap[child + 1]:
            child += 1
        # 힙을 만족시키도록
        if heap[child] > heap[parent]:
            # 둘의 위치를 바꾼다.
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        # 아니면 반복중단
        else:
            break
    return tmp


enq(5)
print(heap[1], heap)
enq(15)
print(heap[1], heap)
enq(8)
print(heap[1], heap)
enq(20)
print(heap[1], heap)
print(deq(), heap)
print(deq(), heap)
print(deq(), heap)

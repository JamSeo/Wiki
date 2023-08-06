import heapq
from copy import deepcopy


def solution(k, n, reqs):
    answer = 1e9
    temp = list([] for _ in range(k + 1))

    for req in reqs:
        *args, category = req
        temp[category].append(req)

    combs = get_partitions(k, n)

    for comb in combs:
        temp_ans = 0
        for i in range(1, k + 1):
            temp_ans += wait_time(comb[i], temp[i])
        answer = min(answer, temp_ans)

    return answer


def get_partitions(k, n):
    partitions = list(map(lambda x: [0] + x, partition(k, n)))

    return partitions


def partition(k, n):
    res = []

    if k == 1:
        return [[n]]

    for num in range(1, n):
        temps = partition(k - 1, n - num)
        for temp in temps:
            res.append([num] + temp)

    return res


def wait_time(n, reqs):
    res = 0
    heap = []
    waitlist = deepcopy(reqs)

    for _ in range(min(n, len(waitlist))):
        s, dt, _ = waitlist.pop(0)
        heapq.heappush(heap, s + dt)

    while waitlist:
        s, dt, _ = waitlist.pop(0)
        e = heapq.heappop(heap)
        wt = e - s if s < e else 0
        res += wt
        heapq.heappush(heap, e + dt)

    return res


print(
    solution(
        3,
        5,
        [
            [10, 60, 1],
            [15, 100, 3],
            [20, 30, 1],
            [30, 50, 3],
            [50, 40, 1],
            [60, 30, 2],
            [65, 30, 1],
            [70, 100, 2],
        ],
    )
)
print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))

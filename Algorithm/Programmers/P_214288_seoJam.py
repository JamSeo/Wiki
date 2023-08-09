import heapq


def solution(k, n, reqs):
    answer = 1e9
    temp = list([] for _ in range(k + 1))
    # [1] 상담 유형별로 구분짓기
    for req in reqs:
        *args, category = req
        temp[category].append(req)
    # [2] 상담 유형별 상담원을 분배하는 모든 경우의 수
    combs = get_partitions(k, n)
    # [3] 각 경우마다 대기시간 구하기
    for comb in combs:
        temp_ans = 0
        for i in range(1, k + 1):
            temp_ans += wait_time(comb[i], temp[i])
            if answer < temp_ans:
                continue
        answer = min(answer, temp_ans)

    return answer


def get_partitions(k, n):
    partitions = list(map(lambda x: [0] + x, partition(k, n)))
    return partitions


# 상담유형별 상담원 배치하는 경우의 수 반환
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
    # 상담원이 더 많은 경우
    if len(reqs) <= n:
        return 0

    res = 0
    heap, waitlist = [0] * n, reqs

    for waiter in waitlist:
        s, dt, _ = waiter
        e = heapq.heappop(heap)
        wt = e - s if s < e else 0  # 대기시간
        res += wt
        e = e + dt if s < e else s + dt  # 상담종료시각
        heapq.heappush(heap, e)

    return res

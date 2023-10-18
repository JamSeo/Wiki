from itertools import permutations


def solution(n, weak, dist):
    answer = 1e9
    len_weak = len(weak)
    len_dist = len(dist)

    # 1. 가능한 점검경로 Array 만들기
    extended_weak = weak + list(map(lambda x: x + n, weak))
    arr_path = [extended_weak[i : i + len_weak] for i in range(len_weak)]

    # 2. dist 순열 만들기
    permutations_worker = list(permutations(dist, len_dist))

    # 3. 순찰하기
    for path in arr_path:
        for arr_worker in permutations_worker:
            idx, count = 0, 0
            for worker in arr_worker:
                # 1명씩 도달가능한 거리만큼 이동
                count += 1
                can_visit = path[idx] + worker
                while idx < len_weak and path[idx] <= can_visit:
                    idx += 1
                # 모든 weak지점을 점검했다면 종료
                if idx == len_weak:
                    answer = min(answer, count)
                    break

    if answer > len_dist:
        return -1

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))

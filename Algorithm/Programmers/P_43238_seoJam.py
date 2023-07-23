# heap으로 시도했다가 50점 맞고 구글링(이분탐색)

def solution(n, times):
    answer = 0
    times.sort()
    left, right = 0, times[-1] * n  # 최선/최악의 심사시간

    while left <= right:
        mid = (left + right) // 2
        immigration = 0             # 심사받는 인원

        for time in times:
            immigration += mid // time

        if n <= immigration:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
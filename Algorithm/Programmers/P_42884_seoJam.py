def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    camera = -30001

    # 다음 차의 진입지점이 현재 차의 진출지점보다 뒤에 있으면? camera +1
    for enter, exit in routes:
        if camera < enter:
            answer += 1
            camera = exit

    return answer

def solution(scores):
    wanho = scores.pop(0)
    sum_wanho = sum(wanho)
    answer, temp = 1, 0

    for score in sorted(scores, key=lambda x: (-x[0], x[1])):
        # [1] 완호가 인센티브 못받을 경우
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        # [2] 인센티브 못받는 사람 거르기
        if score[1] < temp:
            continue
        # [3] 두 점수 합으로 석차 구하기
        if sum_wanho < sum(score):
            answer += 1
            temp = score[1]

    return answer

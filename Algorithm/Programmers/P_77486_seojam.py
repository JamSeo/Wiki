from collections import deque


def solution(enroll, referral, seller, amount):
    referral_dict = dict()
    gain_dict = dict()
    queue = deque([])

    for child, parent in zip(enroll, referral):
        referral_dict[child] = parent
        gain_dict[child] = 0

    for person, gain in zip(seller, amount):
        queue.append((person, gain * 100))

    while queue:
        person, gain = queue.popleft()

        referral_gain = int(gain * 0.1)
        gain_dict[person] += gain - referral_gain
        referral = referral_dict[person]

        if referral_dict[person] != "-" and referral_gain:
            queue.append((referral, referral_gain))

    answer = list(gain_dict.values())

    return answer

# 순열

# nPk -> input_ = k
# a: 현재 만드는 순열, k: 순열의 다음 칸, input_: 만들고자하는 순열의 크기
def backtrack(a, k, input_):
    c = [0] * MAXCANDIDATES
    # k == input_ 일때, 순열에 사용할 데이터 다 고름
    if k == input_:
        for i in range(1, k + 1):
            print(a[i], end = '')
        print()

    # 아직 다 못 골랐어
    else:
        k += 1
        # 다음에 올 수 있는 후보자들 수
        ncandidates = construct_candidates(a, k, input_, c)
        # 후보자들 수만큼 돌리고
        for i in range(ncandidates):
            # 현재 위치에서 후보자 저장하고
            a[k] = c[i]
            # 다음 위치에 뭐 넣을지 돌리자
            backtrack(a, k, input_)

# a: 현재 만드는 순열, k: 순열의 다음 칸,
# input_: 만들고자하는 순열의 크기, c: candidates
def construct_candidates(a, k, input_, c):
    # 순열의 visitied list : 이 숫자가 이미 사용되었는가?
    in_perm = [False] * (NMAX + 1)
    # a를 검사하며 사용됐는지 판단하자.
    # 해당 정보 갱신 : 쓴 적 있으면 True
    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0  # 후보 개수 & c배열의 idx

    for i in range(1, input_ + 1):
        # 사용된 적 없는 숫자
        if not in_perm[i]:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


MAXCANDIDATES = 10
NMAX = 10
a = [0] * (NMAX + 1)
data = [i for i in range(10)]
cnt = 0
total_cnt = 0
backtrack(a, 7, 9)

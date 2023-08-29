def solution(key, lock):
    M, N = len(key), len(lock)
    target = []

    # [0] 새로운 자물쇠 만들기; 기존 자물쇠에 두께 M만큼 패딩하기
    new_lock = [[0] * (2 * M + N) for _ in range(2 * M + N)]

    for i in range(M, M + N):
        for j in range(M, M + N):
            new_lock[i][j] = lock[i - M][j - M]

    # [1] 자물쇠 빈칸 좌표 저장
    for i in range(M, M + N):
        for j in range(M, M + N):
            if new_lock[i][j] == 0:
                target.append((i, j))

    # [2] 브루트 포스
    for _ in range(4):
        key = list(zip(*key[::-1]))  # 90도 회전

        for si in range(1, M + N):
            for sj in range(1, M + N):
                if isRightKey(si, sj, key, new_lock, target):
                    return True

    return False


def isRightKey(si, sj, key, new_lock, target):
    cnt = 0
    M = len(key)

    for i in range(M):
        for j in range(M):
            # key와 lock이 겹치는 경우
            if key[i][j] + new_lock[si + i][sj + j] > 1:
                return False
            # key가 lock이 딱맞는 경우
            if key[i][j] and (si + i, sj + j) in target:
                cnt += 1

            if cnt == len(target):
                return True

    return False

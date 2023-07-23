for _ in range(1, 11):
    tc = int(input())

    a = [list(map(int, input().split())) for _ in range(100)]

    for idx in range(100):  # 사다리 값이 2인 idx를 j에 저장
        if a[99][idx] == 2:
            j = idx

    i = 99
    while i >= 0:  # i : 99 -> 0이 되도록 역사다리 탈거임

        # 왼쪽이 1인 경우, 1이 끝날때 까지 좌로 한 칸씩
        if j > 1 and a[i][j - 1]:
            while j > 1 and a[i][j - 1]:
                j -= 1
            else:
                i -= 1  # while문 끝나면 위로 한 칸

        # 오른쪽이 1인 경우, 1이 끝날때 까지 우로 한 칸씩
        elif j < 99 and a[i][j + 1]:
            while j < 99 and a[i][j + 1]:
                j += 1
            else:
                i -= 1  # while문 끝나면 위로 한 칸

        # 양옆에 1이 없을 경우, 위로 한 칸
        else:
            i -= 1

    print(f'#{tc} {j}')  # 마지막 j값 출력
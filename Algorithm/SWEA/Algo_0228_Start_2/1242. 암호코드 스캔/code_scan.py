# 16진수 -> 2진수 dictionary
hex_to_bin = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}

# 앞쪽 0을 생략한 암호 코드
passcode_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}


def code_scanner(width, height, code):
    answer = 0
    # code의 높이만큼 검증
    # 위쪽 줄을 확인해야 되서 range활용
    for row in range(height):
        # idx는 한 줄에서 지금 확인중인 글자의 인덱스
        idx = width * 4 - 1
        # 암호코드 8자리의 최소길이 == 56, 그때의 암호코드의 시작과 끝 인덱스 == 0 ~ 55
        # 즉 마지막으로 확인할 인덱스는 55
        while idx > 54:  # 보다 작아지면 반복 종료
            # 1을 만나면 검증 시작
            if code[row][idx] and code[row - 1][idx] == 0:
                # 여기서 password 초기화를 한것은
                password = []
                # if 내부에서 8글자를 다 찾을 예정이란 뜻
                for _ in range(8):
                    # (0)101 == (c1 -) c2 - c3 - c4 (각각 0과 1이 몇번 등장했는지)
                    c2 = c3 = c4 = 0

                    # 이전 코드의 1번째 0
                    while code[row][idx] == 0:
                        idx -= 1
                    # 이번 코드의 4번째 부분
                    while code[row][idx] == 1:
                        idx -= 1
                        c4 += 1
                    # 이번 코드의 3번째 부분
                    while code[row][idx] == 0:
                        idx -= 1
                        c3 += 1
                    # 이번 코드의 2번째 부분
                    while code[row][idx] == 1:
                        idx -= 1
                        c2 += 1
                    # 각각의 while은 숫자가 변하는 시점에 종료된다.

                    # 배율을 찾고
                    ratio = min(c2, c3, c4)
                    # 암호에 추가
                    password.append(passcode_dict[(c2 // ratio, c3 // ratio, c4 // ratio)])
                # for문 종료 (8자리 코드 완성)

                # 짤수 & 홀수 자리 검증
                even_digit_sum = password[0] + password[2] + password[4] + password[6]
                odd_digit_sum = password[1] + password[3] + password[5] + password[7]
                if (odd_digit_sum * 3 + even_digit_sum) % 10 == 0:
                    answer += even_digit_sum + odd_digit_sum

            # 검증하지 않아도 앞으로는 가야된다.
            idx -= 1
    # 결과 반환
    return answer


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]

    print(f'#{test_case} {code_scanner(M, N, arr)}')
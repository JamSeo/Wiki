import sys
sys.stdin = open("input.txt")

table = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
         }

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    temp = []
    decode = []
    ans = 0

    # temp 중 1이 있는 리스트만 추출해서 문자열(code)로 저장
    for _ in range(N):
        temp = input()
        if '1' in temp:
            code = temp

    # 문자열 뒤에서부터 table과 일치하는 암호코드를 찾아 해독문(decode) 만들기
    i = M
    decode = ''
    while len(decode) < 8:
        if code[i - 7: i] in table:
            decode = table[code[i - 7: i]] + decode
            i -= 7
        else: i -= 1

    # check_decode: 잘못된 암호코드인지 검증
    check_decode = 0
    decode = list(map(int, decode))
    for idx in range(8):
        if not idx % 2:   # 짝수 idx
            check_decode += 3 * decode[idx]
        else:             # 홀수 idx
            check_decode += decode[idx]

    # ans: 제대로 된 코드면 해독문의 합 출력
    if not check_decode % 10:
        ans = sum(decode)

    print(f'#{tc} {ans}')
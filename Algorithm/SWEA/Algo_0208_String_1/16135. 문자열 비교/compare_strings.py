import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    ans = 0  # 일단 ans는 0으로 저장

    str1 = input()
    str2 = input()

    N1 = len(str1)
    N2 = len(str2)

    for i in range(N2 - N1 + 1):
        arr = str2[i : i + N1]  # arr : string -- str2 속에 str1과 같은 길이를 가진 문자열

        if arr == str1:  # arr이 str1과 같다면 ans를 1로 저장
            ans = 1
            break

    print(f'#{tc} {ans}')
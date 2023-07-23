import sys
sys.stdin = open("sample_input.txt")


T = int(input())  # 테스트케이스: 3

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max_cnt = 0
    for char in str1:
        cnt = str2.count(char)  # str1의 글자별로 cnt 수 저장
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')
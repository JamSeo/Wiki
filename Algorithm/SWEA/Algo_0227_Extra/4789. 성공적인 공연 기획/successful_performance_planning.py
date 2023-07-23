import sys
sys.stdin = open("sample_input.txt")


for tc in range(int(input())):
    arr = list(map(int, input()))
    employ = clap = 0

    for i in range(1, len(arr)):

        clap += arr[i - 1]
        if clap < i:
            employ += i - clap
            clap = i

    print(f'#{tc + 1} {employ}')
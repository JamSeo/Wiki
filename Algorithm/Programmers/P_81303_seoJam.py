# linked_list 문제입니당.
def solution(n, k, cmds):
    linked_list = {i: [i-1, i+1] for i in range(n)}
    arr = ['O'] * n
    del_stack = []  # 삭제칸 저장용 stack

    for _ in cmds:
        cmd = _.split()

        # [1] D: 아래 이동
        if cmd[0] == "D":
            for _ in range(int(cmd[1])):
                k = linked_list[k][1]

        # [2] U: 위 이동
        elif cmd[0] == "U":
            for _ in range(int(cmd[1])):
                k = linked_list[k][0]

        # [3] C: 현재 행 삭제
        elif cmd[0] == "C":
            before, after = linked_list[k]
            arr[k] = 'X'
            del_stack.append((before, k, after))
            # 막행이면 앞으로, 아니면 뒤로 이동
            if after == n:
                k = before
            else:
                k = after
            # 앞 뒤 노드 연결해주기
            if before == -1:
                linked_list[after][0] = -1
            elif after == n:
                linked_list[before][1] = n
            else:
                linked_list[after][0] = before
                linked_list[before][1] = after

        # [4] Z: 삭제 행 복구
        elif cmd[0] == "Z":
            before, temp_k, after = del_stack.pop()
            arr[temp_k] = 'O'
            # 다시 연결
            if before == -1:
                linked_list[after][0] = temp_k
            elif after == n:
                linked_list[before][1] = temp_k
            else:
                linked_list[after][0] = temp_k
                linked_list[before][1] = temp_k

    answer = ''.join(arr)
    return answer

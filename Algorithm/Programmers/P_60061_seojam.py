def solution(n, build_frame):
    wall = []

    for [x, y, obj, build] in build_frame:
        
        if build: 
            wall.append([x, y, obj])  # 설치
        else: 
            wall.remove([x, y, obj])  # 제거


        # 설치 or 제거 후 구조물 상태 확인
        safe = True
        
        for [wx, wy, wobj] in wall:
            # 검사 필요 없는 자재들은 통과 (ref.지현's)
            if wx < x -1 or x + 1 < wx or wy < y -1 or y + 1 < wy:
                continue
            # 기둥 검사
            if wobj == 0:
                if wy == 0 or [wx - 1, wy, 1] in wall or [wx, wy, 1] in wall or [wx, wy - 1, 0] in wall:
                    continue
                safe = False
            # 보 검사
            elif wobj == 1:
                if [wx, wy - 1, 0] in wall or [wx + 1, wy - 1, 0] in wall or ([wx - 1, wy, 1] in wall and [wx + 1, wy, 1] in wall):
                  continue
                safe = False

        if not safe:
            if build: 
                wall.remove([x, y, obj])
            else: 
                wall.append([x, y, obj])

    return sorted(wall)


print(solution(5,	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
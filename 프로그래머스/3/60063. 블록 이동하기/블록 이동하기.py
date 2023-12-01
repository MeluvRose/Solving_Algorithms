from collections import deque

def move(location, board):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    locs = []
    left, right = location
    length = len(board)
    
    # 1칸 이동
    for i in range(4):
        leftY, leftX = left[0] + dy[i], left[1] + dx[i]
        rightY, rightX = right[0] + dy[i], right[1] + dx[i]
        # 경계 안에서, 이동할 위치에 벽이 없으면
        if (0 <= leftY < length and 0 <= leftX < length
           and 0 <= rightY < length and 0 <= rightX < length
           and board[leftY][leftX] == 0
           and board[rightY][rightX] == 0):
            locs.append({(leftY, leftX), (rightY, rightX)});
            
    # 회전
    if left[0] == right[0]: # 로봇이 가로방향이면
        for d in [-1, 1]:
            leftY = left[0] + d
            rightY = right[0] + d
            # 경계 안에서, 회전이 가능하다면
            if (0 <= leftY < length
                and 0 <= rightY < length
                and board[leftY][left[1]] == 0
                and board[rightY][right[1]] == 0):
                locs.append({left, (leftY, left[1])});
                locs.append({right, (rightY, right[1])});
        return locs;
    # 로봇이 세로방향이면
    for d in [-1, 1]: 
        leftX = left[1] + d
        rightX = right[1] + d
        # 경계 안에서, 회전이 가능하다면
        if (0 <= leftX < length
           and 0 <= rightX < length
           and board[left[0]][leftX] == 0
           and board[right[0]][rightX] == 0):
            locs.append({(left[0], leftX), left});
            locs.append({(right[0], rightX), right});
    return locs;
    
def solution(board):
    length = len(board)
    # robots = deque([([[0, 0], [0, 1]], 0)])
    robots = deque()
    visited = [{(0, 0), (0, 1)}]
    
    robots.append(({(0, 0), (0, 1)}, 0));
    while robots:
        location, cnt = robots.popleft();
        
        # 도착
        if (length - 1, length - 1) in location:
            return cnt;
        # 이동
        for robot in move(location, board):
            if robot not in visited: # 아직 방문하지 않은 곳이면
                robots.append((robot, cnt + 1));
                visited.append(robot);
    return 0;

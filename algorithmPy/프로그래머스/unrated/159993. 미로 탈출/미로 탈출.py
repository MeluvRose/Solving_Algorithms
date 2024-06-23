

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def excape(maze, point, exit):
    global dx
    global dy
    queue = deque()
    visited = [[0] * len(maze[0]) 
               for _ in range(len(maze))]
    
    queue.append(point);
    while queue:
        # print(queue, visited);
        y, x = queue.popleft()
        if (maze[y][x] == exit): 
            return visited[y][x];
        # 현 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            # 미로 공간을 벗어난 경우
            if (newX < 0 or newX >= len(maze[0])
               or newY < 0 or newY >= len(maze)):
                continue;
            # print(newY, newX, maze[newY][newX]);
            # 원점으로 돌아오거나 벽인 경우
            if ((newY, newX) == point 
                or maze[newY][newX] == 'X'):
                continue;
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if (visited[newY][newX] == 0):
                visited[newY][newX] = visited[y][x] + 1
                queue.append((newY,newX));
                # print(queue);
    return -1

def solution(maps):
    """
    (S -> L) 까지의 최소거리와
    (L -> E) 까지의 최소거리를
    각각 구하여, 합을 전달해야 한다.
    """
    toL = -1
    toE = -1
    pointS = None
    pointL = None
    maze = []
    
    for idx, m in enumerate(maps):
        v = [0] * len(m)
        m = list(m);
        if 'S' in m : 
            pointS = tuple([idx, m.index('S')]);
        if 'L' in m : 
            pointL = tuple([idx, m.index('L')]);
        maze.append(m);
    # print(maze, pointS, pointL);
    toL = excape(maze, pointS, 'L');
    toE = excape(maze, pointL, 'E');
    if toL < 0 or toE < 0: return -1;
    return toL + toE;
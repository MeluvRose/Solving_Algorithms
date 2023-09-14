from collections import deque

def solution(maps):
    queue = deque()
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols 
               for _ in range(rows)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited[0][0] = True;
    queue.append((0, 0));
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            newY = y + dy[i];
            newX = x + dx[i];
            if (newY < 0 or newY >= rows 
                or newX < 0 or newX >= cols
                or maps[newY][newX] == 0
                or visited[newY][newX] == True):
                continue;
            maps[newY][newX] = maps[y][x] + 1;
            visited[newY][newX] = True;
            queue.append((newX, newY));
    if visited[rows - 1][cols - 1] == False:
        return -1;
    return maps[rows - 1][cols - 1];
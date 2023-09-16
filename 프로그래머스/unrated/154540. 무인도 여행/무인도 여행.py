from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visit = [[False] * cols for _ in range(rows)]
    answer = []
    
    def bfs(maps, row, col):
        queue = deque()
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
        area = int(maps[row][col])
    
        queue.append((row, col));
        visit[row][col] = True;
        while queue:
            y, x = queue.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if (ny < 0 or ny == rows
                   or nx < 0 or nx == cols
                   or visit[ny][nx] == True
                   or maps[ny][nx] == 'X'):
                    continue;
                visit[ny][nx] = True
                area += int(maps[ny][nx])
                queue.append((ny, nx))
        return area
    
    for y in range(rows):
        for x in range(cols):
            if maps[y][x] != 'X' and visit[y][x] == 0:
                answer.append(bfs(maps, y, x));
    if answer: return sorted(answer);
    return [-1];
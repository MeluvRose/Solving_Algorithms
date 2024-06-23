from collections import deque

def solution(board):
    answer = -1
    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def getR(board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'R':
                    return (y, x);
        return (-1, -1);
            
    sy, sx = getR(board)
    queue = deque()
    
    queue.append((sy, sx, 0));
    visited[sy][sx] = True;
    while queue:
        y, x, cnt = queue.popleft()
        dx = 1
        dy = 1
        
        if board[y][x] == 'G':
            answer = cnt;
            break;
        # up
        while (y - dy >= 0 
               and board[y - dy][x] != 'D'): 
            dy += 1;
        if visited[y - dy + 1][x] == False:
            visited[y - dy + 1][x] = True;
            queue.append((y - dy + 1, x, cnt + 1));
        dy = 1;
        # down
        while (y + dy <= rows - 1
               and board[y + dy][x] != 'D'): 
            dy += 1;
        if visited[y + dy - 1][x] == False:
            visited[y + dy - 1][x] = True;
            queue.append((y + dy - 1, x, cnt + 1));
        dy = 1;
        # left
        while (x - dx >= 0 and board[y][x - dx] != 'D'): 
            dx += 1;
        if visited[y][x - dx + 1] == False:
            visited[y][x - dx + 1] = True;
            queue.append((y, x - dx + 1, cnt + 1));
        dx = 1;
        # right
        while (x + dx <= cols - 1 and board[y][x + dx] != 'D'): 
            dx += 1;
        if visited[y][x + dx - 1] == False:
            visited[y][x + dx - 1] = True;
            queue.append((y, x + dx - 1, cnt + 1));
        dx = 1;
    return answer;
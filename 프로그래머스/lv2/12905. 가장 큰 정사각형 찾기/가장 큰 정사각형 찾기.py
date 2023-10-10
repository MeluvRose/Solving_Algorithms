def solution(board):
    line = 0
    rows = len(board)
    cols = len(board[0])
    points = [[0] * (cols + 1) 
              for _ in range(rows + 1)]
    
    """
    # print(board);
    for r in range(rows - 1):
        for c in range(cols - 1):
            if (board[r][c] != 0
               and board[r + 1][c] != 0
               and board[r][c + 1] != 0
               and board[r + 1][c + 1] != 0):
                board[r + 1][c + 1] = board[r][c] + 1;
    for row in board:
    #     print(row);
        maxLen = max(row);
        answer = max(answer, maxLen * maxLen);
    """
    for r in range(rows):
        for c in range(cols):
            points[r + 1][c + 1] = board[r][c];
    for r in range(rows + 1):
        for c in range(cols + 1):
            if points[r][c] != 0:
                points[r][c] = min(
                    min(points[r - 1][c], points[r][c - 1]), points[r - 1][c - 1]
                ) + 1
                line = max(line, points[r][c]);
    # for row in points:
    #     print(row);
    return line * line;
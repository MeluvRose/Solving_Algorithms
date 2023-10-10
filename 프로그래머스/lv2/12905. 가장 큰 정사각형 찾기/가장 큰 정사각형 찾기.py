def solution(board):
    line = 0
    rows = len(board)
    cols = len(board[0])
    points = [[0] * (cols + 1) 
              for _ in range(rows + 1)]
    
    """
    (y, x) 위치의 값은 그것으로 만들 수 있는 최대의 정사각형의 한 변이 되게 만들어보자.
    
    - 왼쪽, 위쪽, 10시 방향의 값 중 최소값 + 1의 값으로 수정하며 진행
    - 단, (y, x) 위치의 값이 0이었다면, 더하지 X
    """
    # 가장 바깥쪽에 있는 좌표를 포함하기 위해,
    # 0으로 감싸는 테두리를 추가
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
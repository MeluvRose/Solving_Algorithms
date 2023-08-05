def solution(park, routes):
    rowIdx = 0;
    colIdx = 0;
    maxRow = len(park)
    maxCol = len(park[0])
    
    for r in range(maxRow):
        for c in range(maxCol):
            if park[r][c] == 'S':
                rowIdx = r;
                colIdx = c;
                break;
    for route in routes:
        y = rowIdx;
        x = colIdx;
        for c in range(int(route[2])):
            if (route[0] == 'E' and x + 1 < maxCol 
                and park[y][x + 1] != 'X'):
                    x += 1;
                    if c == int(route[2]) - 1: colIdx = x;
            if (route[0] == 'W' and x - 1 >= 0 
                and park[y][x - 1] != 'X'):
                    x -= 1;
                    if c == int(route[2]) - 1: colIdx = x;
            if (route[0] == 'S' and y + 1 < maxRow 
                and park[y + 1][x] != 'X'):
                    y += 1;
                    if c == int(route[2]) - 1: rowIdx = y;
            if (route[0] == 'N' and y - 1 >= 0 
                and park[y - 1][x] != 'X'):
                    y -= 1;
                    if c == int(route[2]) - 1: rowIdx = y;
        print(rowIdx, colIdx);
    return [rowIdx, colIdx];

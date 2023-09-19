def solution(grid):
    answer = []
    # 모든 칸에는 4가지 방향의 경로가 존재하고,
    # 격자는 n 개의 행과 m 개의 열로 이뤄져있다고 하자
    rows, cols = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(cols)]
              for _ in range(rows)]
    # D -> L -> U -> R 의 순으로 빛이 
    # 이동하는걸 (예시 그림으로) 확인
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    
    def move(r, c, i):
        dy, dx = directions[i]
        
        return (r + dy) % rows, (c + dx) % cols;
    
    def rotate(d, node):
        if node == 'R': d = (d + 1) % 4;
        elif node == 'L': d = (d - 1) % 4;
        return d;
    
    for r in range(rows):
        for c in range(cols):
            for i in range(4):
                if visited[r][c][i]: continue;
                y, x, d = r, c, i # 상위 반복문에 영향을 주지 않도록
                cnt = 0
                while not visited[y][x][d]:
                    visited[y][x][d] = True; # 방문 처리
                    
                    # 이동은 첫 방향(아래)부터 이뤄지며,
                    # 이동한 칸과 다음 이동 방향 연산한다.
                    cnt += 1;
                    y, x = move(y, x, d);
                    d = rotate(d, grid[y][x]);
                answer.append(cnt);
                
    # 모든 길이를 오름차순 정렬
    return sorted(answer);
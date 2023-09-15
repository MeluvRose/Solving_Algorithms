from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 모든 좌표값은 1 이상 50 이하이며,
    # 2차원 좌표를 행렬로 표현하기 위해선
    # 2배의 좌표값으로 행렬에 그려야 한다.
    # (https://velog.io/@rlaalswn3282/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EC%9D%B4%ED%85%9C-%EC%A4%8D%EA%B8%B0)
    """
    (함수 분할이 왜 안되는가?)
    route = [[-1] * 102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    answer = 51 * 51;
    
    def getRoute(rectangle):
        for r in rectangle:
            # 모든 좌표값의 2배
            x1, y1, x2, y2 = map(lambda x: x*2, r);
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    # if route[y][x] == 0: 
                    #     route[y][x] = 1;
                    # else: route[y][x] = 0;
                    
                    # x1, x2, y1, y2는 테두리이므로 1, 내부는 0으로 채움
                    if x1 < i < x2 and y1 < j < y2:
                        route[i][j] = 0;
                    # 다른 직사각형의 내부가 아니면서 테두리에 해당할 떼,
                    elif route[i][j] != 0: 
                        route[i][j] = 1;
        return; 
    
    def bfs(c, item):
        queue = deque()
        
        queue.append((c[0] * 2, c[1] * 2));
        while queue:
            x, y = queue.popleft();
            # 도착
            if (x == (item[0] * 2)
               and y == (item[1] * 2)):
                answer = visited[y][x] // 2;
                return answer;
            # 4방향 순회(체크)
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                # 현재 좌표가 테두리이고, 아직 방문하지 않은
                # 곳이라면, 그동안의 최단거리로 값을 수정
                if (visited[newY][newX] == 1
                   and route[newY][newX] == 1):
                    visited[newY][newX] = visited[y][x] + 1;
                    queue.append((newX, newY));
    getRoute(rectangle);
    answer = bfs((characterX, characterY),
                 (itemX, itemY));
    return answer;
    """
    answer = 0
    
    # 제한사항에서 모든 좌표값은 1 이상 50 이하라고 했고 2배의 좌표를 그려야 하므로 102*102 크기의 2차원 배열 선언
    field = [[-1] * 102 for i in range(102)]
    
    # 직사각형 그리기
    for r in rectangle:
    	# 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 큐에 캐릭터 출발지점 추가 & 최단거리를 적어줄 visited 배열 선언
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)]
    
    while q:
        x, y = q.popleft()
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        # 아니라면 상하좌우 네 방향을 체크하면서
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer

"""
(example 2)
from collections import deque
answer = 10000
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 여집합으로 모두 면적을 구한 뒤, 테두리만 추출하기.
    # 다른 공식으로 풀 수 있지만, 이 방법은 좌표계에서 최대 크기가 50x50 이다.
    # 그러니 무지성으로 완탐 급으로 돌린다.
    # 하지만 너무 가까운 테두리는 인식이 안될 수도 있다.
    # 그러므로 사이즈는 2배로 늘린다.

    # 각 방향 좌표를 구하기.
    left, bottom, right, top = [100, 100, 0, 0]
    for v in rectangle:
        left = min(left, v[0])
        bottom = min(bottom, v[1])
        right = max(right, v[2])
        top = max(top, v[3])
    top *= 2
    right *= 2
    left *= 2
    bottom *= 2

    # matrix에 여집합으로 매핑하기.
    matrix = [[0 for row in range((right + 2))] for col in range((top + 2))]
    for x1, y1, x2, y2 in rectangle:
        for col in range(y1 * 2, 2 * y2 + 1):
            for row in range(x1 * 2, 2 * x2 + 1):
                matrix[top - col + 1][row] |= 1

    # 테두리만 2로 변경하기.
    matrix = BFS(matrix, top + 2, right + 2)

    # 테두리만 따라가서 길이 추적하기.
    visited = [[False for row in range(right + 2)] for col in range(top + 2)]
    start = [characterX * 2, top - characterY * 2 + 1]
    goal = [itemX * 2, top - itemY * 2 + 1]
    visited[start[1]][start[0]] = True
    DFS(matrix, start, goal, visited, top + 1, right + 1, 0)

    return answer // 2


def BFS(matrix, N, M):
    Queue = deque()

    # mapping to start_x, start_y
    Queue.append([0, 0])
    visited = [[False for row in range(M)] for col in range(N)]

    # 8 arrow
    # format -> right, down, left, up, rightup, rightdown, leftdown, leftup
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    visited[0][0] = True

    while Queue:
        x, y = Queue.popleft()
        for i in range(8):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < M and 0 <= Y < N:
                if visited[Y][X]:
                    continue
                if matrix[Y][X] == 0:
                    Queue.append([X, Y])
                    visited[Y][X] = True
                elif matrix[Y][X] == 1:
                    matrix[Y][X] = 2
                    visited[Y][X] = True

    return matrix


def DFS(matrix, start, goal, visited, N, M, cnt):
    if start == goal:
        global answer
        answer = min(cnt, answer)
        return
    # 4 arrow
    # format -> right, down, left, up
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        X = start[0] + dx[i]
        Y = start[1] + dy[i]
        if 0 <= X < M and 0 <= Y < N:
            if visited[Y][X]:
                continue
            if matrix[Y][X] == 2:
                visited[Y][X] = True
                DFS(matrix, [X, Y], goal, visited, N, M, cnt + 1)
                visited[Y][X] = False
    return
"""
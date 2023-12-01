# from collections import deque

# def solution(board):
#     answer = float("inf");
#     dy = [-1, 1, 0, 0]
#     dx = [0, 0, -1, 1]
#     length = len(board)
#     costs = [[0 for _ in range(length)] 
#         for _ in range(length)] 
    
#     def build():
#         nonlocal answer
#         nonlocal costs
#         paths = deque([[0, 0, -1, 0, 0]])
#         end = length - 1
        
#         while paths:
#             y, x, d, curve, cost = paths.popleft()
#             print(y, x, d, curve, cost);
            
#             if y == end and x == end: # 도착
#                 answer = min(answer, cost);
#                 continue;
            
#             neighbors = [[y + dy[i], x + dx[i]] for i in range(4)]
#             for direction, [newY, newX] in enumerate(neighbors):
#                 # 경계를 벗어났거나 벽을 만났을 때
#                 if (0 > newY or newY > end
#                     or 0 > newX or newX > end
#                     or board[newY][newX] == 1):
#                     continue;
                
#                 # 그 외
#                 expect = cost + 600
#                 newCurve = 1
#                 if (d == -1 or d == direction):
#                     expect -= 500;
#                     newCurve = 0;
#                 if (curve == 1 and curve == newCurve): 
#                     expect -= 100;
#                 if (costs[newY][newX] != 0
#                    and costs[newY][newX] < expect):
#                     continue;
#                 costs[newY][newX] = expect;
#                 paths.append([newY, newX, direction, newCurve, expect]);
    
#     # costs[0][0] = -1;
#     build();
#     return answer;

from heapq import heappop, heappush
from sys import maxsize

def solution(board):
    N = len(board)
    costBoard = [[ [maxsize] * N for _ in range(N) ] for _ in range(4)]
    for i in range(4): costBoard[i][0][0] = 0
    
    # BFS
    heap = [(0, 0, 0, 0), (0, 0, 0, 2)]
    while heap:
        cost, x, y, d = heappop(heap)
        
        # 4방향 이동
        for dx, dy, dd in ((1,0,0),(-1,0,1),(0,1,2),(0,-1,3)):
            nx, ny = x + dx, y + dy
            
            # 경계 침범 or 벽
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx]: continue
            
            # 이동비용 갱신
            newCost = cost + (100 if d == dd else 600)
            
            # 최소비용 갱신
            if costBoard[dd][ny][nx] > newCost:
                costBoard[dd][ny][nx] = newCost
                heappush(heap, (newCost,nx,ny,dd))
                
    return min(costBoard[0][N-1][N-1], costBoard[1][N-1][N-1], costBoard[2][N-1][N-1], costBoard[3][N-1][N-1])
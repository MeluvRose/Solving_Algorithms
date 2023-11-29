# 1. Permutation(순열)을 사용하여 짝지을 카드의 순서를 정한다.
# 2. 모든 경우의 순서에 대해 조작 횟수가 가장 적은 것을 구한다.

from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy

def move_cost(board, start, end):   # 조작 횟수 Count
    if start == end: return 0;
    queue = deque([[start[0], start[1], 0]])
    visit = {start}
    
    # BFS (1칸 이동 -> 가까운 카드로의 이동 순으로 누적 탐색)
    while queue:                    
        x, y, c = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy     # move
            cx, cy = x, y
            while True:             # ctrl + move
                cx, cy = cx+dx, cy+dy;
                if not (0 <= cx <= 3 and 0 <= cy <= 3): # 카드를 못 찾고 판을 벗어나는 경우
                    cx, cy = cx-dx, cy-dy;
                    break;
                if board[cx][cy] != 0: break;

            if (nx, ny) == end or (cx, cy) == end:  # 도착 최단 경로
                return c + 1;

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c+1));
                visit.add((nx, ny));
            if (cx, cy) not in visit:
                queue.append((cx, cy, c+1));
                visit.add((cx, cy));

def solution(board, r, c):
    answer = float('inf')
    dictCard = defaultdict(list)
    
    def flip(board, curr, order, cost):
        if len(order) == 0: return cost   # 모든 카드를 확인한 경우
        card = dictCard[order[0]] # 현재 선택해야 할 카드의 종류

        # 현재위치에서 한 쌍을 뒤집데 필요한 조작 횟수 + 2(카드 선택)
        choice1 = move_cost(board, curr, card[0]) + move_cost(board, card[0], card[1]) + 2
        choice2 = move_cost(board, curr, card[1]) + move_cost(board, card[1], card[0]) + 2

        # 선택한 카드는 board에서 0으로 변경
        new_board = [b[:] for b in board]
        new_board[card[0][0]][card[0][1]] = 0
        new_board[card[1][0]][card[1][1]] = 0

        if choice1 < choice2:   # 적은 조작 횟수를 한 경우를 따라 재귀
            return flip(new_board, card[1], order[1:], cost + choice1)
        return flip(new_board, card[0], order[1:], cost + choice2)
    
    # 카드의 종류에 따라 좌표 저장
    for row in range(4):        
        for col in range(4):
            num = board[row][col]
            if num != 0:
                dictCard[num].append((row, col))
    # 완전 탐색
    length = len(dictCard)
    for order in permutations(range(1, length + 1), length):    
        answer = min(answer, flip(board, (r, c), order, 0))

    return answer
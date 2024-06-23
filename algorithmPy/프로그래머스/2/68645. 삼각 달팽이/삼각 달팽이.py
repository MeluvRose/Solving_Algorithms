def solution(n):
    answer = []
    snail = [[0] * (i + 1) for i in range(n)]
    row, col = -1, 0
    val = 1
    for i in range(n):
        """
        채우기 연산의 방향은 3가지 순서로 반복된다.
        1. 열(row) 이동: row++
        2. 행(col) 이동: col++
        3. 대각선 이동: row-- and col--
        그리고 횟수는 n, n-1, ..., 1만큼 이뤄진다.
        """
        move = n - i;
        for j in range(move):
            if i % 3 == 0: row += 1;
            elif i % 3 == 1: col += 1;
            else:
                row -= 1;
                col -= 1;
            # print(j, [row, col]);
            snail[row][col] = val;
            val += 1;
    # print(snail);
    for s in snail:
        answer.extend(s);
    return answer

"""
(class)
import sys
sys.setrecursionlimit(1000000)

class Triangle():
    def __init__(self,n):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.cnt = 1
        self.answer = []
        self.ldown(0,0,n)
        for i in range(n):
            for j in range(i+1):
                self.answer.append(self.board[i][j])

    def ldown(self,x,y,n):
        if n < 1:
            return 0
        for i in range(x,x+n):
            self.board[i][y] = self.cnt
            self.cnt += 1
        self.right(i,y+1,n-1)

    def right(self,x,y,n):
        if n < 1:
            return 0
        for j in range(y,y+n):
            self.board[x][j] = self.cnt
            self.cnt += 1
        self.lup(x-1,j-1,n-1)

    def lup(self,x,y,n):
        if n < 1:
            return 0
        for i in range(x,x-n,-1):
            self.board[i][y] = self.cnt
            y -= 1
            self.cnt += 1
        self.ldown(i+1,y+1,n-1)

def solution(n):
    triangle = Triangle(n)
    return triangle.answer
"""
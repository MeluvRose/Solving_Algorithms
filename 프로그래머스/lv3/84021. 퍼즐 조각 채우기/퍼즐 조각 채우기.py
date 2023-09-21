"""
"""
from collections import deque

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    def bfs(i, j, data, findit, n, m):
        ret = []
        q = deque([(i, j)])
        data[i][j] = 1 - findit
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while q:
            x, y = q.popleft()
            ret.append((x-i, y-j))
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == findit:
                    q.append((nx, ny))
                    data[nx][ny] = 1 - findit
        return ret
    def rotate_piece(p):
        ret = [p]
        minx = miny = 10 ** 9
        maxx = maxy = -10 ** 9
        for t in p:
            minx = min(minx, t[0])
            miny = min(miny, t[1])
            maxx = max(maxx, t[0])
            maxy = max(maxy, t[1])
        n = maxx - minx + 1
        m = maxy - miny + 1
        mat = [[0] * m for _ in range(n)]
        for t in p:
            mat[t[0]-minx][t[1]-miny] = 1
        # 90
        temp = [[0] * n for _ in range(m)]
        for t in p:
            temp[t[1]-miny][n-1-(t[0]-minx)] = 1
        for i in range(m):
            for j in range(n):
                if temp[i][j] == 1:
                    ret.append(bfs(i, j, temp, 1, m, n))
                    break
        # 270
        temp = [[0] * n for _ in range(m)]
        for t in p:
            temp[m-1-(t[1]-miny)][t[0]-minx] = 1
        for i in range(m):
            for j in range(n):
                if temp[i][j] == 1:
                    ret.append(bfs(i, j, temp, 1, m, n))
                    break
        # 180
        temp = [[0] * m for _ in range(n)]
        for t in p:
            temp[n-1-(t[0]-minx)][m-1-(t[1]-miny)] = 1
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 1:
                    ret.append(bfs(i, j, temp, 1, n, m))
                    break
        return ret
    pieces = []
    puzzles = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                piece = bfs(i, j, table, 1, n, n)
                pieces.append(piece)
            if game_board[i][j] == 0:
                puzzle = bfs(i, j, game_board, 0, n, n)
                puzzles.append(puzzle)
    # print(pieces)
    visit_p = set()
    visit_puzzle = set()
    for i, p in enumerate(pieces):
        # print(rotate_piece(p))
        if i in visit_p:
            continue
        rotate = rotate_piece(p)
        flg = False
        for r in rotate:
            for j, puzzle in enumerate(puzzles):
                if j not in visit_puzzle and puzzle == r:
                    answer += len(puzzle)
                    visit_p.add(i)
                    visit_puzzle.add(j)
                    flg = True
                    break
            if flg:
                break
    # print(puzzles)
    return answer

"""
from collections import Counter
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def neighbors(self):
        return [
            Pos(self.x, self.y - 1),
            Pos(self.x + 1, self.y),
            Pos(self.x, self.y + 1),
            Pos(self.x - 1, self.y),
        ]


def make_tile_from_positions(positions):
    # Smallest possible representation with rotation

    def rotate90(tile):
        return tuple(
            tuple(tile[i][j] for i in range(len(tile)))
            for j in reversed(range(len(tile[0])))
        )

    positions = set(positions)

    xs = [pos.x for pos in positions]
    min_x = min(xs)
    max_x = max(xs)

    ys = [pos.y for pos in positions]
    min_y = min(ys)
    max_y = max(ys)

    tile_representations = [
        tuple(
            tuple(Pos(i, j) in positions for j in range(min_y, max_y + 1))
            for i in range(min_x, max_x + 1)
        )
    ]

    for __ in range(3):
        tile_representations.append(rotate90(tile_representations[-1]))

    return min(tile_representations)


def get_tile_size(tile):
    return sum(sum(row) for row in tile)


def parse_tiles(board, tile_value=1):
    n = len(board)

    # Add sentinel boundaries
    sentinel = 1 - tile_value

    board = [
        [sentinel] * (n + 2),
        *([sentinel] + row + [sentinel] for row in board),
        [sentinel] * (n + 2),
    ]

    # Detect tiles
    tile_positions = []
    for i, j in product(range(1, n + 1), range(1, n + 1)):
        if board[i][j] == tile_value:
            stack = [Pos(i, j)]
            squares = []
            while stack:
                curr = stack.pop()
                board[curr.x][curr.y] = sentinel
                squares.append(curr)
                for neighbor in curr.neighbors():
                    if board[neighbor.x][neighbor.y] == tile_value:
                        stack.append(neighbor)
            tile_positions.append(squares)

    # Make tiles
    tiles = [make_tile_from_positions(p) for p in tile_positions]

    return tiles


def solution(game_board, table):
    tiles = parse_tiles(table, 1)
    empty_spaces = parse_tiles(game_board, 0)

    tile_counter = Counter(tiles)
    empty_space_counter = Counter(empty_spaces)

    used_tiles = tile_counter & empty_space_counter

    return sum(get_tile_size(tile) * occ for tile, occ in used_tiles.items())
"""

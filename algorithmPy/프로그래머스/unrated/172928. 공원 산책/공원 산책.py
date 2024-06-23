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

"""
class Dog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    def move(self, park, direction, distance):
        i, j = self.g[direction]
        x, y = self.x + (i * distance), self.y + (j * distance)
        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]):
            return park
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
            row[y] for row in park[min(self.x, x) : max(self.x, x)]
        ]:
            return park
        park[self.x][self.y] = "O"
        park[x][y] = "S"
        self.x = x
        self.y = y
        return park

    @classmethod
    def detect_start_dogs_location(self, park):
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.detect_start_dogs_location(park)

    dog = Dog(x, y)

    for route in routes:
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance))

    return [dog.x, dog.y]
"""

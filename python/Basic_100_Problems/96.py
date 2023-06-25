"""
부모님과 함께 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
"""

def makeTable():
    height, width = map(int, input().split())
    
    return [[0 for w in range(width)] 
        for h in range(height)]

def getSticks(n):
    sticks = list()
    
    for i in range(n):
        info_stick = list(map(int, input().split()))
        sticks.append(info_stick)
    return sticks

def stageSticks(table, sticks):
    for stick in sticks:
        l = stick[0]
        d = stick[1]
        x = stick[2] - 1
        y = stick[3] - 1
        if d == 0:
            for hide in range(y, y + l):
                table[x][hide] = 1
        else:
            for hide in range(x, x + l):
                table[hide][y] = 1

table = makeTable()
n = int(input())
sticks = getSticks(n)
stageSticks(table, sticks)

for line in table:
    for idx, fill in enumerate(line):
        if idx == len(line) - 1:
            print(fill)
        else:
            print(fill, end=' ')




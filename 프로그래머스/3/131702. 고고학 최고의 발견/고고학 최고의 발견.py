"""
1. 시계를 돌리는 순서는 답에 영향을 주지 않는다
ex) (0,0) (0,1) (1,0) 번타일을 어떤 순서로 눌러도 
각 시계들을 돌린 횟수들이 같다면 같은 결과 이다

2. 같은 시계를 4번 이상 돌리는 것은 무의미한 일이다 같은 시계를 4번이상 돌리면 
원래 값으로 회귀 하므로 돌리지 않은 것과 같다

3. 맨 윗번줄 시계를 돌린 횟수에 의해 나머지 행의 시계를 몇번 돌려야 하는지 결정 된다
ex) 3x3 시계 집합 에서 첫 행을 각각 a b c 번 돌려 12 시 3시 6시의 결과를 얻었다면
다음 행에서 각각 시계를 0번 3번 2번 돌려야 처음 행의 시계가 모두 12를 가르키게 된다

4. n 번째 행의 m 번째 열의 시계는 n+1 행의 m 번쨰 열의 시계를 돌린 것의 의해 
결과가 종속적으로 변경 되게 된다

< 접근 >
- 주어진 'clockhands'의 길이를 보면, 원소의 최대 개수는 64개
    - '완전 탐색'으로도 충분히 풀이가 가능할 것
    
- 1칸에서의 상태는 총 4가지, 최대 경우의 수 4^(8*8)
    - 모든 경우를 완전히 탐색하는 것은 불가능
    - 돌리려는 n행의 회전 수는 (n-1)행의 회전 수에 의해 결정된다. (종속)
        - 따라서, 1개의 행의 회전 수를 정하는 최대 경우의 수 4^8 만 보면 된다.
"""

from itertools import product
import sys

def solution(clockHands):
    answer = sys.maxsize
    lenClock = len(clockHands)
    dy = [-1, 1, 0, 0, 0]
    dx = [0, 0, -1, 1, 0]
    
    def rotate(a, b, t, arr):
        for k in range(5):
            y, x = a + dy[k], b + dx[k]
            if (0 <= y < lenClock
               and 0 <= x < lenClock):
                arr[y][x] = (arr[y][x] + t) % 4
    
    for case in product(range(4), repeat=lenClock): # 중복 순열
        arr = [hand[:] for hand in clockHands] # 깊은 복사(Slicing)
        result = 0
        
        # 1. 첫번째 줄을 회전
        for i in range(lenClock):
            rotate(0, i, case[i], arr);
            result += case[i]; # 이 회전의 조작 횟수 누적
        
        # 2. 이후 줄에서의 회전
        for i in range(1, lenClock): # 두번째부터
            for j in range(lenClock):
                # 바로 위의 시계가 12시가 아니라면,
                if arr[i - 1][j]:
                    require = 4 - arr[i - 1][j]
                    rotate(i, j, require, arr); # 지금 시계에서의 회전
                    result += require; # 이 회전의 조작 횟수 누적
        
        # 마지막 라인에 12시를 향하지 않는 시계가 존재
        if sum(arr[lenClock - 1]) > 0: continue;
        # 위 과정에서 전 시계가 12시를 향하게 한 횟수 중 최소를 구함
        answer = min(answer, result);
    return answer
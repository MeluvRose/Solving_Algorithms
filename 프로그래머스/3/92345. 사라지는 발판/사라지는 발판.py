# 발판이 있거나 없거나
# 보드 내에서 발판이 있는 곳으로만 이동 가능
# 밟고 있는 발판은 다른 발판을 밞음과 동시에 사라짐
# 자신의 차례에 상하좌우로 인접한 4개의 칸 중
# 발판이 있는 칸으로 옮겨야 한다.
# 더 이상 이동할 수 없거나, 같은 공간에 서있다가
# 누군가 먼저 이동해서 발판이 사라지는 경우 패배
# 양 플레이어가 최적의 플레이를 했을 때 이동한 횟수를 구하시오

def solution(board, aloc, bloc):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    temp = [b[:] for b in board]
    answer = -1
    
    def OOB(y, x):
        return (y < 0 or y >= len(temp)
               or x < 0 or x >= len(temp[0]));
    
    def dfs(aloc, bloc):
        nonlocal temp
        result = 0
        
        # 현 플레이어가 밟을 발판이 사라진다면
        if temp[aloc[0]][aloc[1]] == 0:
            return 0;
        # 네 방향으로의 이동
        for idx in range(4):
            newY = aloc[0] + dy[idx]
            newX = aloc[1] + dx[idx]
            if OOB(newY, newX) or temp[newY][newX] == 0:
                continue;
            
            # 플레이어 방문
            temp[aloc[0]][aloc[1]] = 0
            move = dfs(bloc, [newY, newX]) + 1 # A, B 번갈아 가며 이동, 회귀를 통해 방문 횟수는 누적 
            temp[aloc[0]][aloc[1]] = 1
            
            # 진행된 턴 횟수에 따라 홀수면 패배, 짝수면 승리
            if result % 2 == 0 and move % 2 == 1: result = move; # 경우가 서로 다르면 갱신
            if result % 2 == 0 and move % 2 == 0: result = max(result, move); # 서로 지는 경우라면 최대한 늦게 지는걸 선택
            if result % 2 == 1 and move % 2 == 1: result = min(result, move); # 서로 이길 경우라면 최대한 빨리 이기는걸 선택
        return result;
    
    answer = dfs(aloc, bloc);
    return answer;
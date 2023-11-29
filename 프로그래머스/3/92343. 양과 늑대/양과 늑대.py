# 이 문제는 dfs를 통한 완전 탐색이긴 하지만,
# 각 탐색 분기의 결과는 서로 독립적이고
# 서로 비교되는 대상에 해당한다.

def solution(info, edges):
    answer = 0
    visited = [False for i in range(len(info))] # 방문 확인을 위한 배열
    
    def solve(visited, search):
        nonlocal answer
        idx = search[0]
        cntSheep = search[1]
        cntWolf = search[2]
        
        visited[idx] = True; # 방문 확인
        
        # 양과 늑대 마리 수 비교
        if info[idx] == 1:
            cntWolf += 1;
            if cntSheep <= cntWolf: 
                return;
        if (info[idx] == 0):
            cntSheep += 1;
            if (cntSheep > answer):
                answer = cntSheep;
        
        # 탐색
        for edge in edges:
            if (visited[edge[0]] and not visited[edge[1]]): # 깊이순으로 탐색하도록 제한
                # 탐색 순서에 따라 방문 여부, 그 시점에서의 마리 수가 달라짐
                nextVisited = visited[:]; 
                solve(nextVisited, 
                      [edge[1], cntSheep, cntWolf]);
    
    solve(visited, [0, 0, 0]);
    return answer;
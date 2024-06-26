"""
이 문제는 dfs(bfs)를 통한 완전 탐색이긴 하지만,
각 탐색 분기의 결과는 서로 독립적이고
서로 비교되는 대상에 해당한다.
"""

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

"""
(BFS)
from collections import deque

def solution(info, edges):
    hash = {}
    for i in range(len(info)):
        hash[i] = []

    for s, e in edges:
        hash[s].append(e)
        hash[e].append(s)

    # bfs
    queue = deque()
    visited = [[0] * (1 << 17) for _ in range(len(info))]

    # cur, sheep, wolf, visited
    queue.append([0, 1, 0, 1])
    visited[0][1] = True;

    answer = 0

    while len(queue) > 0:
        cur, s, w, mask = queue.popleft()
        answer = max(answer, s)
        for node in hash[cur]:
            ns = nw = 0
            if info[node] == 0 and mask & (1 << node) == 0:
                ns = 1
            if info[node] == 1 and mask & (1 << node) == 0:
                nw = 1

            if s <= w + nw:
                continue

            nmask = mask | (1 << node)

            if visited[node][nmask]:
                continue

            visited[node][nmask] = True
            queue.append([node, s + ns, w + nw, nmask])

    return answer
"""
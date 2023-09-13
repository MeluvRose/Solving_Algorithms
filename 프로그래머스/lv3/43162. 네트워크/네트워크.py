from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == True:
            continue;
        visited[i] = True;
        queue.append(i);
        answer += 1;
        while queue:
            i = queue.popleft();
            for j in range(n):
                if (computers[i][j] == 1
                   and visited[j] == False):
                    visited[j] = True;
                    queue.append(j);
    return answer

"""
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(i, n, visited):
        for j in range(n):
            if (computers[i][j] == 1
               and visited[j] == False):
                visited[j] = True;
                dfs(j, n, visited);
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True;
            answer += 1;
            dfs(i, n, visited);
    return answer;
"""
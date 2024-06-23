def solution(tickets):
    lenTickets = len(tickets)
    visited = [False] * lenTickets
    answer = []
    
    def dfs(current, path):
        # 모든 티켓을 사용한 경로에는
        # (티켓 수 + 1)만큼의 공항을 방문한다.
        if len(path) == lenTickets + 1:
            answer.append(path);
            return;
        
        for t in range(lenTickets):
            if (tickets[t][0] == current
               and visited[t] == False):
                visited[t] = True;
                dfs(tickets[t][1], path + [tickets[t][1]]);
                visited[t] = False;
        return;
    
    dfs("ICN", ["ICN"]);
    # print("before :", answer);
    answer.sort();
    # print("after :", answer);
    return answer[0];

"""
(Hint)
https://school.programmers.co.kr/learn/courses/14743/lessons/118891
"""

"""
(BFS)
from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN",["ICN"], []))
    
    while q:
        airport, path, used = q.popleft()

        if len(used) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))
                
    
    answer.sort()

    return answer[0]
"""
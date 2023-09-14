def solution(tickets):
    lenTickets = len(tickets)
    visited = [False] * lenTickets
    answer = []
    
    def dfs(current, path):
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
    
    # tickets.sort(key=lambda x:x[1]);
    dfs("ICN", ["ICN"]);
    answer.sort();
    return answer[0];

"""
(Hint)
런타임에러와 중복된 티켓팅을 생각해야 1,2번 테케를 통과할 수 있습니다
"""
def dfs(n, computers, nodes):
    computer = computers[nodes[-1]];
    visit = 0
    
    if n == len(nodes):
        return nodes;
    for idx in range(len(computer)):
        if (computer[idx] == 1
           and idx not in nodes):
            nodes.append(idx);
            return dfs(n, computers, nodes);
        else: visit += 1;
    if visit == len(computer):
        return nodes;
        

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
    networks = []
    
    for i in range(len(computers)):
        net = dfs(n, computers, [i]);
        # print("net :", net);
        net.sort();
        if len(net) == n: return 1;
        if net not in networks:
            networks.append(net);
    # print("networks :", networks);
    answer = len(networks);
    """
    return answer
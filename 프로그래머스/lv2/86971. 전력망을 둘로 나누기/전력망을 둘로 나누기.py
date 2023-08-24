from collections import deque, defaultdict

def solution(n, wires):
    # answer = n
    routes = [[] for _ in range(n + 1)]
    vals = [defaultdict(int) for _ in range(n + 1)]
    
    # 전력망을 인접 리스트로 표현
    for i, j in wires:
        routes[i].append(j)
        routes[j].append(i)
    tovisit = deque(range(n))
    minv = n
    while len(tovisit) > 1:
        cn = tovisit[-1]
        # print(tovisit, cn);
        # print(routes[cn], vals[cn]);
        if len(routes[cn]) == len(vals[cn])+1:
            tovisit.pop()
            v = 1
            for i in routes[cn]:
                if not vals[cn][i]:
                    nn = i
                v += vals[cn][i]
            vals[nn][cn] = v
            minv = min(minv, abs(n-2*v))
        tovisit.rotate()
    return minv
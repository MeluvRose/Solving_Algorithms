from collections import deque, defaultdict

def solution(n, wires):
    # answer = n
    wires = [[l - 1, r - 1] for l, r in wires]
    routes = [[] for _ in range(n)]
    vals = [defaultdict(int) for _ in range(n)]
    
    # 전력망을 인접 리스트로 표현
    for i, j in wires:
        routes[i].append(j)
        routes[j].append(i)
    tovisit = deque(range(n))
    minv = n
    while len(tovisit) > 1:
        cn = tovisit[-1]
        # print(tovisit, cn);
        if len(routes[cn]) == len(vals[cn])+1:
            # print(cn, routes[cn], vals[cn]);
            tovisit.pop() # 이미 확인한 탑(노드)는 제거 
            v = 1
            for i in routes[cn]:
                print(i, vals[cn], end = ' > ')
                if not vals[cn][i]:
                    nn = i
                v += vals[cn][i]
            print(nn, cn, v);
            vals[nn][cn] = v
            minv = min(minv, abs(n-2*v))
        tovisit.rotate()
    return minv

"""
from collections import defaultdict, deque

def BFS(n, startNode, arr, check):
    cnt = 1
    que = deque([startNode])
    visited = [True for _ in range(n+1)]
    visited[startNode] = False

    while que:
        node = que.popleft()
        for target in arr[node]:
            if check[node][target] and check[target][node] and visited[target]:
                visited[target] = False
                que.append(target)
                cnt += 1

    return cnt

def solution(n, wires):
    answer = n
    arr = defaultdict(list)
    check = [[False for _ in range(n+1)] for _ in range(n+1)]

    for wire in wires:
        arr[wire[0]].append(wire[1])
        arr[wire[1]].append(wire[0])
        check[wire[0]][wire[1]] = True
        check[wire[1]][wire[0]] = True

    for i, wire in enumerate(wires):
        a,b = wire
        check[a][b] = False
        check[b][a] = False
        answer = min(answer, abs(BFS(n, a, arr, check) - BFS(n, b, arr, check)))
        check[a][b] = True
        check[b][a] = True

    return answer
"""

"""
(Union find)
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer
"""
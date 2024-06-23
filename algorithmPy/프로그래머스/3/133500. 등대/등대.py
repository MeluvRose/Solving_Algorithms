# 모든 등대(노드)의 상태는 켜짐 or 꺼짐

# 1. 자식과 부모 노드 모두의 불이 꺼져 있다면
# 부모 노드의 불을 키면서, 켜진 등대 개수 구하기

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

def solution(n, lighthouse):
    answer = 0
    isLightOn = [False] * n
    dictLight = defaultdict(list)
    
    def initDictLight(lighthouse):
        for l, r in lighthouse:
            dictLight[l].append(r);
            dictLight[r].append(l);
    
    def dfs(node, parent):
        nonlocal answer;
        
        for num in dictLight[node]:
            if num != parent:
                dfs(num, node);
                # 자식과 부모 둘 다 꺼져 있다면, 부모 불 켜주기
                if (isLightOn[num - 1] == False 
                    and isLightOn[node - 1] == False):
                    isLightOn[node - 1] = True;
                    answer += 1;
    
    initDictLight(lighthouse);
    dfs(1, 1);
    return answer;

"""
# 2. 각각 노드에서 그 노드가 켜져있을 때의 최소 개수
# 그 노드가 꺼져있을 때의 최소 개수를 각각 구함

import sys
from collections import defaultdict
sys.setrecursionlimit(1000001)

A = defaultdict(list)
vis = [False] * 1000001

# 자신을 포함한 subtree에서, 내가 켜졌을 때의 최소 점등 등대 개수와
# 내가 꺼졌을 때의 최소 점등 등대 개수를 반환합니다.
def dfs(u):
    vis[u] = True
    if not A[u]:
        # u가 leaf라면 내가 켜졌을 떄의 최소 점등 등대 개수는 1
        # 내가 꺼졌을 때의 최소 점등 등대 개수는 0
        return 1, 0
    
    # u가 leaf가 아니라면
    on, off = 1, 0
    for v in [v for v in A[u] if not vis[v]]:
        # 내가 켜졌다면 child들은 켜지든 꺼지든 상관 없습니다. -> 킨 것과 끈 것중 최소값을 취함
        # 내가 꺼졌다면 child들은 무조건 켜져야 합니다.
        # 이 점을 생각해서 leaf들의 정보를 취합, 정리합니다.
        child_on, child_off = dfs(v)
        on += min(child_on, child_off)
        off += child_on
    return on, off

def solution(n, lighthouse):
    for u, v in lighthouse:
        A[u].append(v)
        A[v].append(u)
        
    on, off = dfs(1)
    return min(on, off)
"""
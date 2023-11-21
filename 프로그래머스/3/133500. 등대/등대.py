# 모든 등대(노드)의 상태는 켜짐 or 꺼짐

# 1. 자식과 부모 노드 모두의 불이 꺼져 있다면
# 부모 노드의 불을 키면서, 켜진 등대 개수 구하기

# 2. 각각 노드에서 그 노드가 켜져있을 때의 최소 개수
# 그 노드가 꺼져있을 때의 최소 개수를 각각 구함

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
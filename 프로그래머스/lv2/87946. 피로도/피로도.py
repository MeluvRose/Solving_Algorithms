from itertools import permutations

"""
dungeons 배열의 요소의 수가 가변적이고, 
순서가 정해져있지 않는 경우의 수들을 구해야하므로
중첩 for문을 활용한 경우의 수 구하기는 (저로써는) 힘들다고 봅니다.

파이썬을 사용하시는 프로그래머라면 itertools 라이브러리의 permutations를 사용하여 한 번에 dungeons에 대한
모든 경우의 수를 구할 수 있습니다. 순서대로 돌려서 제일 많이 던전에 방문할 수 있는 경우를 반환하시면 됩니다.

만약 경우의 수를 직접 구현하고 싶으시다면, dfs나 bfs방법으로 직접 구하셔서 값을 구하시면 됩니다.
"""

def solution(k, dungeons):
    answer = -1
    cases = []
    
    # 모든 (경우의 수의) 조합을 구한다  
    for cnt in range(len(dungeons), 1, -1):
        for i in permutations(dungeons, cnt):
            cases.append(i);        
    for case in cases:
        present = k;
        cnt = 0
        
        # 현재 조합에서 탐험을 순차적으로 진행
        for least, consume in case:
            if (present >= least):
                present -= consume;
                cnt += 1;
        # 하나의 조합에서 모두 탐험이 가능한 경우
        if cnt == len(case):
            answer = cnt;
            break;
    return answer

"""
(resursion)

solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
"""

"""
(dfs, (backtracking))

answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
"""

"""
(permutation)

from itertools import permutations
# 8! = 40320. 무지성 순열 가즈아
def solution(k, dungeons):
    ans = 0
    pList = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    for p in pList:
        curK = k # 초기 피로도
        cnt = 0. # 탐험한 던전 수
        for i in range(len(p)): # 무지성 탐색
            if curK < dungeons[p[i]][0] or curK < dungeons[p[i]][1]: # 해당 던전을 탐사할 수 없을 때 종료
                break
            # "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다. -> 최소 피로도만 넘으면 항상 탐사 가능
            curK -= dungeons[p[i]][1] # 소모 피로도만큼 감소
            cnt += 1 # 던전 탐험
        ans = max(ans, cnt) # 최대값 갱신
    return ans
"""
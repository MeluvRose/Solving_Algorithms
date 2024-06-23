def solution(n, info):
    answer = []
    board = [0] * 11
    maxDiff = 0
    
    def isBetter(ryan):
        last = len(ryan) - 1
        
        while last >= 0:
            if ryan[last] > answer[last]:
                return True;
            elif ryan[last] < answer[last]:
                return False;
            last -= 1;
    
    def calcScore(ryan, apeach):
        nonlocal answer
        nonlocal maxDiff
        rScore, aScore = 0, 0
        diff = None
        
        for i in range(11):
            if ryan[i] > apeach[i]:
                rScore += 10 - i;
            elif apeach[i] > 0:
                aScore += 10 - i;
        diff = rScore - aScore;
        if diff > 0 and diff >= maxDiff:
            if (diff == maxDiff
               and not isBetter(ryan)): return;
            maxDiff = diff;
            answer = ryan[:];
    
    def search(n, info, idx):
        if (n == 0 or idx == len(info)):
            board[-1] += n;
            calcScore(board, info);
            board[-1] -= n;
            return;
        
        # 점수를 얻기로 결정
        if n > info[idx]:
            board[idx] += info[idx] + 1;
            search(n - board[idx], info, idx + 1);
            board[idx] -= info[idx] + 1;
        
        # 얻지 않기로 결정
        search(n, info, idx + 1);
         
    search(n, info, 0);
    if not answer: return [-1];
    return answer;

"""
(DFS)
def solution(n, info):
    global answer, result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global answer, result
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    result = 0
    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]
"""

"""
(itertools)
from itertools import product
def solution(n, info):
    info.reverse()
    ans = [-1]
    maxd = 0
    for wl in product((True, False), repeat=11):
        t = 0
        s = sum(info[i]+1 for i in range(11) if wl[i])
        if s <= n:
            apeach = sum(i for i in range(11) if not wl[i] and info[i])
            ryan = sum(i for i in range(11) if wl[i])
            d = ryan-apeach
            if d > maxd:
                maxd = d
                ans = [info[i]+1 if wl[i] else 0 for i in range(11)]
                ans[0] += n-s
    ans.reverse()
    return ans;
"""
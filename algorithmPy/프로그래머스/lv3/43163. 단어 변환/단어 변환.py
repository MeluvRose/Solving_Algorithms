from collections import deque

# 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
transistable = lambda a,b: sum(
    (1 if x!=y else 0) for x,y in zip(a,b)) == 1;

def solution(begin, target, words):
    queue = deque()
    d = dict()
    
    queue.append((begin, 0));
    # 'words'의 요소들은 filter의 x가 되어, 함수
    # 'transistable' 를 통해 filter가 실행된다.
    d[begin] = set(filter(
        lambda x:transistable(x, begin), words));
    for w in words:
        d[w] = set(filter(lambda x:transistable(x,w), words));
    while queue:
        current, level = queue.popleft()
        # 탐색 깊이가 'words' 길이보다 클 경우
        if level > len(words): return 0;
        for w in d[current]:
            if w == target: return level + 1;
            else: queue.append((w, level + 1));
    return 0;
"""
(DFS)
def solution(begin, target, words):
    lenWords = len(words)
    answer = lenWords + 1
    flag = 0
    visited = [False] * lenWords;
    
    def dfs(word, target, level):
        # 'visited', 'words'의 경우, 
        # 전혀 다른 list를 새로 대입(할당)
        # 하는 것이 아니기 때문에
        # nonlocal로 선언하지 않아도 O(?)
        nonlocal flag, lenWords, answer
        
        if word == target:
            flag = 1
            answer = min(answer, level)
            return;
        for i in range(lenWords):
            cnt = 0
            # 한 개의 알파벳만 바꿀 수 있는지 체크
            for j in range(len(word)):
                if word[j] != words[i][j]: 
                    cnt += 1;
            if (visited[i] == False 
                and cnt == 1):
                visited[i] = True;
                dfs(words[i], target, level + 1);
                visited[i] = False;
                
    dfs(begin, target, 0);
    if flag: return answer;
    return 0;
"""
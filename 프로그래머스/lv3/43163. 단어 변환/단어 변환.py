def solution(begin, target, words):
    lenWords = len(words)
    answer = lenWords + 1
    flag = 0
    visited = [False] * lenWords;
    
    def dfs(word, target, level):
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

# def differ(s1, s2):
#     result = 0
    
#     for n in range(len(s1)):
#         if s1[n] != s2[n]:
#             result += 1;
#     return result;

# def transition(begin, target, words):
#     result = len(words) + 1;
#     visited = None
#     stack = []
    
#     for w in words:
#         if differ(begin, w) != 1:
#             continue;
#         visited = [w];
#         stack.append(w);
#         while stack:
#             last = stack[-1]
#             if last == target:
#                 result = min(len(stack), result); 
#                 stack.pop();
#             if visited == words: break;
#             for new in words:
#                 if (differ(last, new) == 1
#                    and new not in visited):
#                     visited.append(new);
#                     stack.append(new);
#                     break;
#     if result > len(words): return 0;
#     return result;
        

# def solution(begin, target, words):
#     answer = 0
    
#     if target not in words: return answer;
#     answer = transition(begin, target, words);
#     return answer;
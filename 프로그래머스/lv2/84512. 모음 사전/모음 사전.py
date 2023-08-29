def getWords(s):
    result = [];
    
    # print(result, s);
    if len(s) < 5:
        arr = ['A', 'E', 'I', 'O', 'U']
        for c in arr:
            result.append(s + c);
            result += getWords(s + c);
    else: result.append(s)
    return result;
def solution(word):
    # answer = findWord("")
    answer = 0
    words = getWords("")
    
    words = list(set(words));
    answer = sorted(words).index(word) + 1;
    return answer
def getWords(s):
    result = [];
    
    if len(s) < 5:
        arr = ['A', 'E', 'I', 'O', 'U']
        for c in arr:
            result.append(s);
            result += getWords(s + c);
    else: result.append(s)
    return result;

def solution(word):
    answer = 0
    words = getWords("")
    
    words = list(set(words));
    answer = sorted(words).index(word);
    return answer

"""
(product)
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
"""

"""
(등비 수열)
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer
"""
def solution(number):
    answer = 0
    lenNumber = len(number);
    
    for a in range(lenNumber):
        for b in range(a + 1, lenNumber):
            for c in range(b + 1, lenNumber):
                if (number[a] + number[b] 
                    + number[c] == 0): 
                    answer += 1;
    return answer

"""
def solution(number):
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt
"""
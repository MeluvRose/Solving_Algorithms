import math

def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k):
        # points.append(_);
        maxY = math.sqrt((d*d) - (x*x));
        answer += (maxY // k) + 1;
    return answer;
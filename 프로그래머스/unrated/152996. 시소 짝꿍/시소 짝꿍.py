from collections import defaultdict

def solution(weights):
    answer = 0
    scales = defaultdict(int)
    
    weights.sort();
    for w in weights:
        answer += scales[w];
        answer += scales[w / 2];
        answer += scales[w * 2 / 3];
        answer += scales[w * 3 / 4];
        scales[w] += 1;
    return answer
def solution(n, m, section):
    answer = 0
    
    start = section[0];
    answer += 1;
    for s in section:
        if start + m > s: continue;
        start = s;
        answer += 1;
    return answer
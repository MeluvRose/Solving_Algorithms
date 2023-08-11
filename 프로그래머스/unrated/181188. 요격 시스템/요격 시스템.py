def solution(targets):
    answer = 0
    # l = 0
    # r = 0
    x = 0;
    
    targets.sort(key=lambda x: x[1]);
    # print(targets);
    for t in targets:
        l = t[0]
        r = t[1]
        if (l >= x):
            x = r;
            answer += 1;
    return answer
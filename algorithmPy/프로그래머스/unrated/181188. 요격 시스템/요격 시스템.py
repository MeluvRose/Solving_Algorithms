def solution(targets):
    answer = 0
    x = 0
    
    # targets.sort() (X)
    targets.sort(key=lambda x: x[1]);
    """
    첫 미사일을 기준으로 새로운 미사일이 이전
    미사일의 좌표 범위를 벗어나는 지를 확인하게
    될 것이기에 target([s,e])의 e 좌표를 기준
    으로 정렬했어야 하는 이유이다.
    """
    # print(targets);
    for t in targets:
        l = t[0]
        r = t[1]
        if (l >= x):
            x = r;
            answer += 1;
    return answer
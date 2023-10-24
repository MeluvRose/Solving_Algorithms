def solution(n, stations, w):
    answer = 0
    idx = 0
    
    i = 1
    while i <= n:
        # 현재 위치에서 전파가 닿을 때,
        if (idx < len(stations)
            and i >= stations[idx] - w):
            # 위치를 전파가 안 닿는 곳까지 이동
            i = stations[idx] + w + 1;
            idx += 1;
        # 현재 위치에서 전파가 안 닿을 때,
        else:
            # 현재 위치를 포함해서, 전파 범위만큼 이동
            # (새로운 기지국이 이 범위만큼 전파가 가능하다고 가정)
            i += w * 2 + 1;
            answer += 1;
    return answer;
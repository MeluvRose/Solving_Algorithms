"""
1. 새로운 기지국은 전파가 닿지 않는 아파트에 필요
2. 기존에 설치된 기지국을 기준으로 구역을 나눠준다.
    (만약, stations의 길이가 m이라면, m + 1의 구역이 나올 것)
3. 나눠준 구역은 전부 빈 공간이기에 그 공간에 필요한 최소 기지국
수를 구함
"""

def solution(n, stations, w):
    answer = 0
    idx = 0
    
    i = 1
    while i <= n:
        if (idx < len(stations)
            and i >= stations[idx] - w):
            i = stations[idx] + w + 1;
            idx += 1;
        else:
            answer += 1;
            i += w * 2 + 1;
    return answer;
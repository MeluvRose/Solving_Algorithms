"""
1. 서로 다른 10개 : 50
2. (캐시: 3) 같은 3개 쌍이 3개 : 21
3. [제주, 판교] (10) > [판교, 서울] (15)
> [서울, 뉴욕] (20) > [뉴욕, 엘에이] (25)
> [엘에이, 샌프란] (30) > 

이전에 존재하는 값이면(cache hit), 실행시간 1
이전에 존재하지 않는 값이면(cache miss), 실행시간 5
"""
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cacheQueue = deque()
    
    # 캐시 사이즈가 0일 때,
    if cacheSize == 0:
        answer = 5 * len(cities);
        return answer;
    # 도시 이름이 대소문자를 구분하지 않으므로,
    # 비교 전, 우선 대문자로 통일한다.
    cities = [c.upper() for c in cities];
    # 캐시 사이즈가 0 이상일 때,
    for c in cities:
        # 캐시에 존재한다면, 캐시에서 제거한 후,
        # 캐시의 맨 뒤에 다시 추가(LRU(?))
        if c in cacheQueue:
            cacheQueue.remove(c);
            cacheQueue.append(c);
            answer += 1;
            continue;
        answer += 5;
        if (len(cacheQueue) >= cacheSize):
            cacheQueue.popleft();
        cacheQueue.append(c);
    return answer;
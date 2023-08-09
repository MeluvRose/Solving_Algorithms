def solution(people, limit):
    answer = 0
    weight = limit
    left = 0
    right = len(people) - 1
    
    people.sort();
    """
    # 첫 번째 풀이
    while len(people) > 1:
        w = people[len(people) - 1]
        if (weight - w) >= 0:
            people.pop();
            weight -= w;
        else: 
            weight = limit;
            answer += 1;
            cnt = 0;
    if len(people) == 1: answer += 1;
    
    # P1. 최적의 '조합'이 될 수 있는 경우를
    # 만들었어야 했다.
    # >> 인원 제한을 고려하지 X, 만약 없었더라도
    # 1명이 아닌 여러 명이 탑승 가능했기에, 아직
    # 더 근사한 값을 만들어낼 수 없는 지 확인
    # 했어야 했다.
    # P2. 'Greedy'를 사용하고자 할 경우, 요소
    # 들의 '정렬' 여부를 확인하여야 한다.
    """
    while left <= right:
        # 조건에 제일 최적화된 값을 우선 고려한다.
        weight -= people[right]
        right -= 1;
        # 매번, 조건과 (가능한) 제일 근접한 근사치를 만들어 내야 한다.
        # 무게 제한 외에 인원 제한 또한 최대 2명이므로, 
        # 1명 더 탈 수 있는지 또한, 확인해야 한다.
        if weight >= people[left]: left += 1;
        answer += 1;
        weight = limit;
    return answer;

"""
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
"""
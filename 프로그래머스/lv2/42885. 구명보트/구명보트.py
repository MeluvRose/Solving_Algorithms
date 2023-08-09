def solution(people, limit):
    answer = 0
    weight = limit
    left = 0
    right = len(people) - 1
    
    people.sort();
    # while len(people) > 1:
    #     w = people[len(people) - 1]
    #     if (weight - w) >= 0:
    #         people.pop();
    #         weight -= w;
    #     else: 
    #         weight = limit;
    #         answer += 1;
    #         cnt = 0;
    # if len(people) == 1: answer += 1;
    
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
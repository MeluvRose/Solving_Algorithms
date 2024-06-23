def solution(priorities, location):
    answer = 0
    idxs = [i for i in range(len(priorities))]
    
    while priorities:
        val = priorities.pop(0)
        idx = idxs.pop(0)
        
        if priorities and val < max(priorities):
            priorities.append(val);
            idxs.append(idx);
            continue;
        answer += 1;
        if idx == location: break;
    return answer
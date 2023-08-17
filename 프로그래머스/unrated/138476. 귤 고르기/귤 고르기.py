def solution(k, tangerine):
    answer = 0
    dictTangerine = {}
    
    for t in tangerine:
        if t not in dictTangerine.keys():
            dictTangerine[t] = 1;
            continue;
        dictTangerine[t] += 1;
    counts = list(dictTangerine.values());
    counts.sort();
    while counts:
        count = counts.pop();
        k -= count;
        answer += 1;
        if k <= 0: break;
    return answer
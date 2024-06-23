def solution(k, tangerine):
    answer = 0
    dictTangerine = {}
    
    # (크기:개수)의 쌍으로 dict 생성
    for t in tangerine:
        if t not in dictTangerine.keys():
            dictTangerine[t] = 1;
            continue;
        dictTangerine[t] += 1;
    # 개수가 많은 순으로 정렬
    counts = list(dictTangerine.values());
    counts.sort();
    # 목표 개수를 채울 동안 필요한 개수 채우기
    # 이 때, 크기는 신경쓰지 않아도 O
    while counts:
        count = counts.pop();
        k -= count;
        answer += 1;
        if k <= 0: break;
    return answer
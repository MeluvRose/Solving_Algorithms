def solution(cards):
    answer = 0
    lenCards = len(cards)
    groups = []
    opens = [0 for _ in range(lenCards)]
    
    idx = 0
    group = []
    while (0 in opens or idx < lenCards):
        if opens[idx] == 0:
            opens[idx] = 1;
            group.append(cards[idx]);
            idx = cards[idx] - 1;
            continue;
        if not group: idx += 1;
        else:
            groups.append(group[:]);
            idx = 0;
            group = [];
    if (len(groups) < 2): return answer;
    groups.sort(key=lambda x: -len(x));
    answer = len(groups[0]) * len(groups[1]);
    return answer
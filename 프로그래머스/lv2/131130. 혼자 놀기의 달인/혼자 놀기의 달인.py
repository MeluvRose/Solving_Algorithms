def solution(cards):
    answer = 0
    lenCards = len(cards)
    groups = [] # 열린 상자 그룹들의 집합
    opens = [0 for _ in range(lenCards)] # 열림 확인
    
    idx = 0
    group = []
    # 모든 상자들이 열려 있는지, 
    # 그리고 모든 인덱스에서 확인을 진행했는지
    while (0 in opens or idx < lenCards):
        # 현재 확인하려는 박스가 닫혀 있을 때
        if opens[idx] == 0:
            opens[idx] = 1;
            group.append(cards[idx]);
            idx = cards[idx] - 1;
            continue;
        # 아직 열어본 박스가 없을 때
        if not group: idx += 1;
        else:
            groups.append(group[:]);
            idx = 0;
            group = [];
    # 열린 상자의 그룹이 둘 이상이 아닐경우 
    if (len(groups) < 2): return answer;
    # 모든 그룹에서 상자를 가장 많이 열었을
    # 2가지 경우의 수로 최고 점수 계산
    groups.sort(key=lambda x: -len(x));
    answer = len(groups[0]) * len(groups[1]);
    return answer
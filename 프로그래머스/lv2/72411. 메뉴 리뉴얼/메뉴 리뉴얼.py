from itertools import combinations
from collections import Counter

"""
Counter 생성자는 여러 형태의 데이터를 인자로 받는데요. 먼저 
중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 
나오는지가 저장된 객체를 얻게 됩니다.
"""

def solution(orders, course):
    answer = []
    menus = []
    
    # 개수 별 코스 메뉴 조합 구하기
    for c in course:
        temp = []
        
        for order in orders:
            # 주문이 항상 순서대로 배치되어 있지 X : 정렬 필요
            p = combinations(sorted(order), c)
            temp += list(p);
        # print(temp);
        counter = Counter(temp);
        
        # 코스의 메뉴 개수를 충족시키지 못하거나
        # 2명 이상의 손님으로부터 주문이 될 수 없는 경우
        if (len(counter) == 0 
            or max(counter.values()) < 2):
            continue;
        # print(counter);
        # 동일한 메뉴 개수라면, 더 많이 주문될 수 있는 것을 선택
        answer += [''.join(item) for item in counter 
                   if counter[item] == max(counter.values())]
    return sorted(answer);

"""
def solution(orders, course):
    answer = []
    menus = []
    visited = []
    
    def goodCourse(orders, menus, i, strC):
        lenStrC = len(strC)
        
        if lenStrC == course[i]:
            cntGood = 0
            for o in orders:
                cnt = 0
                # print(strC);
                for c in strC:
                    if c in o: cnt += 1
                if cnt == lenStrC: cntGood += 1;
            if cntGood >= 2: answer.append(strC);
            return;
        for idx, menu in enumerate(menus):
            strC += menu;
            goodCourse(orders, menus[idx + 1:], i, strC);
            strC = strC[:-1];
        if i < len(course) - 1:
            goodCourse(orders, menus, i + 1, strC);
    
    for o in orders:
        menus += list(o);
        menus = list(set(menus));
    menus.sort();
    # print(menus);
    
    goodCourse(orders, menus, 0, "");
    # print(answer);
    return answer;
"""
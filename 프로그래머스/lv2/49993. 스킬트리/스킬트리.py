def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        orders = list(skill);
        cnt = 0;
        for v in tree:
            if v in orders:
                if v == orders[0]: orders.pop(0);
                else: break;
            cnt += 1;
        if cnt == len(tree): answer += 1;
    return answer
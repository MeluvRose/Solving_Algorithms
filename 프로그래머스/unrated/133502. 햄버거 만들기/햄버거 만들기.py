def solution(ingredient):
    answer = 0
    idx = 0
    tmp = ingredient[:]
    arrBurgur = [1, 2, 3, 1];
    
    while idx < len(tmp):
        if (tmp[idx:idx + 4] == arrBurgur):
            # for i in range(4): del tmp[idx];
            del tmp[idx : idx + 4];
            answer += 1;
            if idx > len(tmp):
                idx = 0;
            else:
                idx -= 3;
            # idx = 0;
            continue;
        idx += 1;
    return answer
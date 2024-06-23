"""
def solution(ingredient):
    answer = 0
    idx = 0
    tmp = ingredient[:]
    arrBurgur = [1, 2, 3, 1];
    
    while idx < len(tmp):
        # 특정 인덱스에서 버거의 재료순으로 일치하는 지 확인
        if (tmp[idx:idx + 4] == arrBurgur):
            # 버거의 재료 개수 만큼 해당 인덱스에서 삭제
            # for i in range(4): del tmp[idx];
            del tmp[idx : idx + 4];
            answer += 1;
            # 남은 재료의 개수가 버거의 최소 재료수 보다
            # 많다면, 바로 이전 인덱스부터 다시 확인
            if idx < len(tmp):
                idx -= 3;
            else:
                idx = 0;
            continue;
        idx += 1;
    return answer
"""

def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt
def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    arrCnt = [0 for _ in range(3)]
    cnt = 0
    
    for a in answers:
        if p1[cnt % len(p1)] == a:
            arrCnt[0] += 1;
        if p2[cnt % len(p2)] == a:
            arrCnt[1] += 1;
        if p3[cnt % len(p3)] == a:
            arrCnt[2] += 1;
        cnt += 1;
    for idx, v in enumerate(arrCnt):
        if v == max(arrCnt): answer.append(idx + 1);
    return sorted(answer);
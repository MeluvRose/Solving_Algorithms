def solution(order):
    answer = 0
    idx = 0
    lenOrder = len(order)
    sub = []
    
    for i in range(lenOrder):
        if (i + 1 == order[idx]):
            answer += 1;
            idx += 1;
            while sub and sub[-1] == order[idx]:
                answer += 1;
                idx += 1;
                sub.pop();
        else: sub.append(i + 1);
    # while sub: main.append(sub.pop());
    # for idx, val in enumerate(main):
    #     if (val == order[idx]): answer += 1;
    #     else: break;
    return answer;
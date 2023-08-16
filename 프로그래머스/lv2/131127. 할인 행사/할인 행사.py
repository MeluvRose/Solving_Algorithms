def solution(want, number, discount):
    answer = 0
    lenDiscount = len(discount)
    
    for d in range(lenDiscount - 9):
        sales = [0 for i in range(len(want))]
        for i in range(d, d + 10):
            if discount[i] in want:
                idx = want.index(discount[i])
                sales[idx] += 1;
        if sales == number: answer += 1;
    return answer
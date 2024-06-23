def solution(prices):
    lenPrices = len(prices)
    answer = [0 for i in range(lenPrices)]
    idxStack = []
    
    for idx in range(lenPrices):
        while (idxStack 
            and prices[idxStack[-1]] > prices[idx]):
            i = idxStack.pop();
            answer[i] = idx - i;
        idxStack.append(idx);
    lenStack = len(idxStack)
    for i in range(lenStack):
        idx = idxStack.pop();
        answer[idx] = (lenPrices - 1) - idx; 
    return answer
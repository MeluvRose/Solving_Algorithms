from collections import deque

def arrSum(arr):
    result = 0
    
    for i in arr: result += i;
    return result;
    
def solution(queue1, queue2):
    answer = 0
    sum1 = arrSum(queue1)
    sum2 = arrSum(queue2)
    limit = len(queue1) * 4;
    
    queue1 = deque(queue1);
    queue2 = deque(queue2);
    if (sum1 + sum2) % 2 == 1: return -1;
    while sum1 != sum2:
        if answer >= limit: return -1;
        elif sum1 > sum2:
            val = queue1.popleft();
            sum1 -= val;
            sum2 += val;
            queue2.append(val);
        else: 
            val = queue2.popleft();
            sum2 -= val;
            sum1 += val;
            queue1.append(val);
        answer += 1;
    return answer
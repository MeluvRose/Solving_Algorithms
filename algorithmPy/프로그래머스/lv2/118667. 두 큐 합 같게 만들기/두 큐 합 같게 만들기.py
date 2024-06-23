from collections import deque
    
def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    # 모든 원소가 같은 위치까지 이동할 만한 횟수로 제한
    limit = len(queue1) * 3
    answer = 0
    
    # pop(0)보다 더 빠른 popleft()를 사용하기 위한
    # deque로 전환
    queue1 = deque(queue1);
    queue2 = deque(queue2);
    # 모든 큐의 값의 합이 홀수면 절대 가능하지 X
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
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    """
    *l하는 이유는 'l' 안의 원소들을 
    하나씩 풀어야 product가 가능
    (컨테이너 타입의 데이터를 Unpacking)
    """
    s = list(map(sum, product(*l)))
    return s.count(target);
"""
(recursion)
def solution(numbers, target):
    if not numbers:
        if target == 0: return 1;
        return 0;
    return (solution(numbers[1:], target - numbers[0]) 
            + solution(numbers[1:], target + numbers[0]));
"""    
    
"""
(mine)
answer = 0

def bfs(numbers, depth, value, target):
    global answer
    
    if depth >= len(numbers):
        if value == target:
            answer += 1;
        return;
    else:
        bfs(numbers, (depth + 1), 
            (value + numbers[depth]), target);
        bfs(numbers, (depth + 1), 
            (value - numbers[depth]), target);

def solution(numbers, target):
    global answer
    
    bfs(numbers, 0, 0, target);
    return answer
"""
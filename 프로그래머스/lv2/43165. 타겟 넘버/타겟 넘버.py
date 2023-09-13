def solution(numbers, target):
    if not numbers:
        if target == 0: return 1;
        return 0;
    return (solution(numbers[1:], target - numbers[0]) 
            + solution(numbers[1:], target + numbers[0]));
"""
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
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
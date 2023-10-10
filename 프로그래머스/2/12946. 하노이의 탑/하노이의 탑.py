"""
i) 원판이 3개 있다고 가정하면,
가장 큰 원판을 제외한 2개의 원판을 '2'번에 옮기고,
이후, 가장 큰 원판을 '3'번에 옮기고, '2'번에 있는
나머지 2개를 '3'번에 옮기는 작업을 실행하면 된다.
ii) 원판이 4개 있다고 가정하면,
가장 큰 원판을 제외한 3개의 원판을 '2'번에 옮기고,
이후, 가장 큰 원판을 '3'번에 옮기고, '2'번에 있는
나머지 3개를 '3'번에 옮기는 작업을 실행하면 된다.

(The reason why you should use 'regression')
여기서 중요한 지점은,
원판의 개수가 N개 일 때, (N - 1)개의 원판을 옮기는
작업이 2회, 가장 큰 원판을 옮기는 작업이 1회가 필요
하다는 것이며,
(N - 1)개의 원판을 옮기는 작업의 최소 횟수는,
(N - 2)개의 원판을 옮기는 작업의 최소 횟수를 알면
구할 수 있다는 것이다. 
"""

def solution(n):
    answer = []
    
    # start: 시작, to: 도착
    def move(start, to):
        answer.append([start, to]);
        
    # n: 원판의 개수, start: 시작, to: 도착, via: 경유지
    def hanoi(n, start, to, via):
        if n == 1:
            move(start, to);
        else:
            # 가장 마지막을 제외한 원판들을 중간에 옮긴다.
            hanoi(n - 1, start, via, to);
            move(start, to);
            # 중간에 둔 원판들을 마지막에 옮긴다.
            hanoi(n - 1, via, to, start);
    
    hanoi(n, 1, 3, 2);
    return answer;
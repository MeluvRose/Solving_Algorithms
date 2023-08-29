from itertools import permutations

"""
dungeons 배열의 요소의 수가 가변적이고, 
순서가 정해져있지 않는 경우의 수들을 구해야하므로
중첩 for문을 활용한 경우의 수 구하기는 (저로써는) 힘들다고 봅니다.

파이썬을 사용하시는 프로그래머라면 itertools 라이브러리의 permutations를 사용하여 한 번에 dungeons에 대한
모든 경우의 수를 구할 수 있습니다. 순서대로 돌려서 제일 많이 던전에 방문할 수 있는 경우를 반환하시면 됩니다.

만약 경우의 수를 직접 구현하고 싶으시다면, dfs나 bfs방법으로 직접 구하셔서 값을 구하시면 됩니다.
"""

def solution(k, dungeons):
    answer = -1
    cases = []
    
    # 모든 (경우의 수의) 조합을 구한다  
    for cnt in range(len(dungeons), 1, -1):
        for i in permutations(dungeons, cnt):
            cases.append(i);        
    for case in cases:
        present = k;
        cnt = 0
        
        # 현재 조합에서 탐험을 순차적으로 진행
        for least, consume in case:
            if (present >= least):
                present -= consume;
                cnt += 1;
        # 하나의 조합에서 모두 탐험이 가능한 경우
        if cnt == len(case):
            answer = cnt;
            break;
    return answer
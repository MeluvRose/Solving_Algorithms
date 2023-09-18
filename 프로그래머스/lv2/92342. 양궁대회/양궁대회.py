# def solution(n, info):
#     answer = []
#     board = [0] * 11
#     score = 0
    
#     def solve(n, info, board, )
#     return answer

"""
라이언 - 전우승자, 어피치 - 결승전 상대
운영위원회: "한 선수의 연속 우승보다는 다양한 선수들이
            우승하길 바래..."

- 규칙
    1. 어피치가 n발을 쏜 후에 라이언이 n발을 쏜다.
    2. 점수를 계산
        - 점수 k는 1 ~ 10점
        - 동일한 점수 구간에 더 많은 화살을 맞췄을
        경우에 해당 점수를 획득한다.
        (단, 적중 횟수에 따른 차등은 X, 해당 점수만을
        획득)
        - 모든 과녁 점수를 총합, 최종 점수를 계산
    3. 더 높은 점수가 더 높은 선수가 우승
    * 점수 계산 시, 동일한 조건일 경우 상대인 
    '어피치'에게 점수를 부여
    우승 판단 또한, 마찬가지 이다.
    
- 결론 : 라이언과 어피치가 쏘게 된 화살 개수(n)과
어피치가 맞힌 과녁의 점수를 10부터 내림차순으로 담은
정수 배열(info)가 주어질 때, 라이언이 가장 큰 점수차로
우승하기 위한 과녁의 점수를 내림차순으로 배열에 담아
반환한다.
(부가 조건)
1. 우승할 수 있는 방법이 여러가지일 경우, 가장 낮은 점수를
더 많이 맞힌 경우의 배열을 반환

2.우승할 수 없는 경우엔 [-1]을 반환
"""

def solution(n, info):
    answer = []
    board = [0] * 11
    maxDiff = 0
    
    def isBetter(ryan):
        last = len(ryan) - 1
        
        while last >= 0:
            if ryan[last] > answer[last]:
                return True;
            elif ryan[last] < answer[last]:
                return False;
            last -= 1;
    
    def calcScore(ryan, apeach):
        nonlocal answer
        nonlocal maxDiff
        rScore, aScore = 0, 0
        diff = None
        
        for i in range(11):
            if ryan[i] > apeach[i]:
                rScore += 10 - i;
            elif apeach[i] > 0:
                aScore += 10 - i;
        diff = rScore - aScore;
        if diff > 0 and diff >= maxDiff:
            if (diff == maxDiff
               and not isBetter(ryan)): return;
            maxDiff = diff;
            answer = ryan[:];
    
    def search(n, info, idx):
        if (n == 0 or idx == len(info)):
            board[-1] += n;
            calcScore(board, info);
            board[-1] -= n;
            return;
        
        # 점수를 얻기로 결정
        if n > info[idx]:
            board[idx] += info[idx] + 1;
            search(n - board[idx], info, idx + 1);
            board[idx] -= info[idx] + 1;
        
        # 얻지 않기로 결정
        search(n, info, idx + 1);
         
    search(n, info, 0);
    if not answer: return [-1];
    return answer;
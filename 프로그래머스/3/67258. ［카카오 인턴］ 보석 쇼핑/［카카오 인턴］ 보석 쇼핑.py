"""
gems : 보석이 종류에 상관없이 일정 개수만큼 진열

구매자인 어피치는 특정 범위의 진열 상품을 연속적으로
모두 구매하려 한다.
이 때, 진열대에 진열되어 있는 모든 종류의 보석을 1개
이상 구매할 수 있는 가장 최적의 범위는?
(가장 좁은 범위가 여러 개 있다면, 진열대 번호가 제일
낮은 범위(구간)을 구한다.)
"""

def solution(gems):
    answer = [0] * 2
    kind = len(list(set(gems))) # 종류 수
    dictGems = {}
    maxLen = 100000 # gems 배열의 최대 크기
    
    start = 0
    for end in range(len(gems)):
        if gems[end] not in dictGems.keys():
            dictGems[gems[end]] = 1;
        else: dictGems[gems[end]] += 1;
        
        # 처음 봤던 보석이 지금은 2개 이상일 때,
        while dictGems[gems[start]] > 1:
            dictGems[gems[start]] -= 1;
            start += 1;
        if (len(dictGems.keys()) == kind
           and maxLen > end - start):
            maxLen = end - start;
            answer[0] = start + 1;
            answer[1] = end + 1;
    return answer;
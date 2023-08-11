def solution(storey):
    answer = 0
    button = 1
    
    
    while (storey > 0):
        button = storey % 10
        
        storey //= 10;
        if (button > 5 
            or (button == 5 and storey % 10 >= 5)):
            button = 10 - button;
            storey += 1;
        answer += button;
    return answer


""" 
# 내가 생각했던 가장 단순한 알고리즘
while ((storey / button) >= 10):
    button *= 10;
while (storey != 0):
    storey = abs(storey) - button;
    if abs(storey) <= (button / 2): 
        button /= 10;
    print(storey, button);
    answer += 1;
"""
    
"""
# 정답이지만 제출 코드보다 약간 긴 코드
while storey != 0:
    n = storey % 10 

    if n >= 6:
        storey += 10 - n
        answer += 10 - n
    elif n == 5 and (storey // 10) % 10 >= 5:
        storey += 10 - n
        answer += 10 - n
    else:
        answer += n
    storey = storey // 10
"""

"""
# 재귀의 활용(?!)
def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))
"""
def solution(storey):
    answer = 0
    button = 1
    
    # while ((storey / button) >= 10):
    #     button *= 10;
    # while (storey != 0):
    #     storey = abs(storey) - button;
    #     if abs(storey) <= (button / 2): 
    #         button /= 10;
    #     print(storey, button);
    #     answer += 1;
    
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
def solution(storey):
    answer = 0
    while storey != 0:
        n = storey % 10 

        if n >= 6:
            storey += 10 - n;
            answer += 10 - n;
        elif n == 5 and (storey // 10) % 10 >= 5:
            storey += 10 - n;
            answer += 10 - n;
        else:
            answer += n;
        storey = storey // 10;
    return answer
"""
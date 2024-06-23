def solution(numbers):
    answer = 0
    dictNum = {key:False for key in range(10)}
    
    for n in numbers: dictNum[n] = True;
    for key in dictNum.keys():
        if (dictNum[key] == False):
            answer += key;
    return answer
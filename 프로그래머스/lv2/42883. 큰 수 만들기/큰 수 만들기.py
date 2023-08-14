def solution(number, k):
    answer = ''
    stack = []
    
    for i in range(len(number)):
        #print('depth : ', i)
        #print('k : ', k)
        #print('stack : ', stack)
        while (stack and stack[-1] < number[i] 
               and k > 0):
            k -= 1
            stack.pop()
        stack.append(number[i])
    # 제거 횟수를 다 사용하지 않았을때 남은 횟수만큼 리스트 뒷부분을 잘라 준다
    if k != 0:
        stack = stack[:-k]
    answer = ''.join(stack);
    return answer
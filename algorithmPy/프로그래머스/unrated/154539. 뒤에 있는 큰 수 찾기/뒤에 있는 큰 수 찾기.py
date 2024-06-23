def solution(numbers):
    lenNumbers = len(numbers);
    answer = [-1 for i in range(lenNumbers)];
    # 비교를 진행했던 index 값을 저장해둘 배열(stack)
    stack = [] 
    
    for i in range(lenNumbers):
        # 'stack' 이 빈 배열이 아니고,
        # 가장 최근의 idx의 numbers 값과 지금 numbers 값을 비교,
        # 조건에 따라 더 이상 비교할 수 없을 때까지 진행
        while stack and numbers[stack[-1]] < numbers[i]:
            # 최근의 idx 값이 지금 값보다 적다면, 지금의 값을
            # 정답 배열의 idx에 지금의 값을 대입, 동시에
            # 저장해둔 idx 값을 순차적 삭제
            answer[stack.pop()] = numbers[i];
        stack.append(i)
    return answer
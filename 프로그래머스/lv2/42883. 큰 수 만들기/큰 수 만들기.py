def solution(number, k):
    answer = ''
    # arrNum = list(number);
    stack = []
    
    # for _ in range(k):
    #     for idx in range(len(arrNum) - 1):
    #         if (arrNum[idx] < arrNum[idx + 1]):
    #             arrNum.pop(idx);
    #             break;
    # answer = answer.join(arrNum);
    for n in number:
        if not stack:
            stack.append(n);
            continue;
        while stack and k > 0:
            if stack[-1] < n:
                stack.pop();
                k -= 1;
            else: break;
        stack.append(n);
        if len(stack) == len(number) - k:
            break;
    answer = answer.join(stack);
    return answer
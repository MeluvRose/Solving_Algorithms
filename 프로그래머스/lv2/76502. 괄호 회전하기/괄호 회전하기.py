def solution(s):
    answer = 0
    lenS = len(s)
    
    for i in range(lenS):
        rotate = []
        for j in range(i, lenS + i):
            if j > (lenS - 1): j -= lenS;
            rotate.append(s[j]);
        # print(rotate, end = ' ')
        # for cnt in range(len(rotate)):
            # part = rotate.pop()
            if (len(rotate) > 1):
                if ((rotate[-1] == '}' and rotate[-2] == '{')
                    or (rotate[-1] == ']' and rotate[-2] == '[')
                    or (rotate[-1] == ')' and rotate[-2] == '(')):
                        rotate.pop();
                        rotate.pop();
        # print(rotate)
        if len(rotate) == 0: answer += 1;
    return answer
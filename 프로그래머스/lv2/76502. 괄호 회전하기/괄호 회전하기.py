def solution(s):
    answer = 0
    lenS = len(s)
    
    for i in range(lenS):
        rotate = []
        cnt = 0
        for j in range(i, lenS + i):
            if j > (lenS - 1): j -= lenS;
            if (s[j] == ')' or s[j] == ']' or s[j] == '}'):
                if (len(rotate) == 0): break
                else:
                    if ((rotate[-1] == '{' and s[j] == '}')
                        or (rotate[-1] == '[' and s[j] == ']')
                        or (rotate[-1] == '(' and s[j] == ')')):
                            rotate.pop();
                    else: break;
            else: rotate.append(s[j]);
            cnt += 1;
        if (cnt == lenS and len(rotate) == 0): answer += 1;
    return answer
"""
for i in range(lenS):
        rotate = []
        for j in range(i, lenS + i):
            if j > (lenS - 1): j -= lenS;
            rotate.append(s[j]);
            if (len(rotate) > 1):
                if ((rotate[-1] == '}' and rotate[-2] == '{')
                    or (rotate[-1] == ']' and rotate[-2] == '[')
                    or (rotate[-1] == ')' and rotate[-2] == '(')):
                        rotate.pop();
                        rotate.pop();
        if len(rotate) == 0: answer += 1;
"""
def solution(X, Y):
    answer = ''
    dictCounts = {}
    
    for c in Y:
        if (c not in dictCounts.keys()):
            dictCounts[c] = 1;
        else:
            dictCounts[c] += 1;
    for c in X:
        if (c in dictCounts.keys()
           and dictCounts[c] != 0):
            dictCounts[c] -= 1;
            answer += c;
    if answer == '' : return "-1";
    output = sorted(list(answer), reverse=True);
    if output[0] == '0': return "0";
    answer = ''.join(output);
    return answer

"""
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
"""
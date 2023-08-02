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
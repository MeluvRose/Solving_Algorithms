import re

def solution(new_id):
    answer = ''
    p = re.compile("[0-9a-z-_.]");
    
    for c in new_id:
        if (c >= 'A' and c <= 'Z'):
            c = chr(ord(c) + 32);
        if (p.match(c) == None):
            continue;
        if (c == '.'):
            if (answer == '' or 
                c == answer[len(answer) - 1]):
                continue;
        answer += c;
    if answer == '' : answer = 'a';
    if len(answer) > 15: answer = answer[:15];
    if answer[0] == '.': answer = answer[1:];
    if answer[-1] == '.': answer = answer[:-1];
    if len(answer) < 3:
        while(len(answer) != 3):
            answer += answer[-1];
    return answer
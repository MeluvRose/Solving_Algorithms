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

"""
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
"""
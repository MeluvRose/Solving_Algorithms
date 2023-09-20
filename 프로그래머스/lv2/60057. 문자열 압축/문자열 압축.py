"""
1. 문자열의 분할은 절반의 길이를 넘을 수 없다.
2. 
"""

def solution(s):
    lenS = len(s)
    answer = lenS * 2 if lenS > 1 else 1
    
    for sep in range(1, lenS // 2 + 1):
        compress = ""
        idx = 0
        sepWord = ""
        cnt = 0
        while (1):
            if idx >= lenS:
                if cnt > 1: compress += f"{cnt}{sepWord}"
                else: compress += sepWord;
                break;
            if sepWord != s[idx:(idx + sep)]:
                if cnt > 0:
                    if cnt > 1: compress += f"{cnt}{sepWord}"
                    else: compress += sepWord;
                sepWord = s[idx:(idx + sep)];
                cnt = 1
            else: cnt += 1;
            idx += sep;
        answer = min(answer, len(compress));
    return answer
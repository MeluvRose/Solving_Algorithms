def palindromeLength(s, i):
    lenS = len(s)
    result = 0
    
    # 최대 길이가 홀수일 때
    left, right = i, i
    while (left >= 0 and right < len(s)
          and s[left] == s[right]):
        left -= 1;
        right += 1;
    result = right - left - 1;
    # 최대 길이가 짝수일 때
    left, right = i, i + 1
    while (left >= 0 and right < len(s)
          and s[left] == s[right]):
        left -= 1;
        right += 1;
    result = max(result, right - left - 1);
    return result;

def solution(s):
    answer = 0
    lenS = len(s)
    
    if lenS <= 1: return lenS;
    for i in range(lenS):
        answer = max(answer, palindromeLength(s, i));
    return answer
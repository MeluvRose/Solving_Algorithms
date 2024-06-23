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

"""
(recursion, java)
class Solution {
    public int solution(String s) {
        int answer = 0;

        for(int i=1; i<=(s.length()/2)+1; i++){
            int result = getSplitedLength(s, i, 1).length();
            answer = i==1 ? result : (answer>result?result:answer);
        }

        return answer;
    }

    public String getSplitedLength(String s, int n, int repeat){
        if(s.length() < n) return s;
        String result = "";
        String preString = s.substring(0, n);
        String postString = s.substring(n, s.length());

        // 불일치 -> 현재까지 [반복횟수 + 반복문자] 조합
        if(!postString.startsWith(preString)){
            if(repeat ==1) return result += preString + getSplitedLength(postString, n, 1);
            return result += Integer.toString(repeat) + preString + getSplitedLength(postString, n, 1);
        }

        return result += getSplitedLength(postString, n, repeat+1);
    }
}
"""
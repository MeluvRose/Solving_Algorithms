def solution(survey, choices):
    answer = ''
    dictKakao = {"RT" : [0 for i in range(2)],
                "CF" : [0 for i in range(2)],
                "JM" : [0 for i in range(2)],
                "AN" : [0 for i in range(2)],}
    
    for idx, s in enumerate(survey):
        kType = s[1] if choices[idx] > 4 else s[0]
        score = (choices[idx] - 4 if choices[idx] > 4
                else 4 - choices[idx])
        
        for key in dictKakao.keys():
            if kType in key:
                dictKakao[key][key.index(kType)] += score;
    for key in dictKakao.keys():
        idx = dictKakao[key].index(max(dictKakao[key]))
        
        answer += key[idx];
    return answer
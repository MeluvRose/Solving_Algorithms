def solution(keymap, targets):
    answer = []
    dictKey = {}
    
    for key in keymap:
        for idx, k in enumerate(key):
            if((k not in dictKey.keys())
              or idx + 1 < dictKey[k]):
                dictKey[k] = idx + 1;
    for target in targets:
        count = 0;
        for c in target:
            if c not in dictKey.keys():
                count = -1;
                break;
            count += dictKey[c];
        answer.append(count);
    return answer;
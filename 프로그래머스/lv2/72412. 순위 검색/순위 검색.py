from itertools import combinations

def getCorrects(values, standard):
    start = 0
    end = len(values);
    
    if end == 0: return end;
    while start < end:
        mid = (start + end) // 2
        
        if values[mid] >= standard: end = mid;
        else: start = mid + 1;
    return len(values) - start;
#     lenValues = len(values);
#     mid = lenValues // 2
    
#     if (mid > 0 and values[mid] >= standard):
#         return getCorrects(values[:mid], standard) + mid;
#     while (mid < lenValues 
#            and values[mid] < standard):
#         mid += 1;
#     if mid == lenValues: return 0;
    # return len(values[mid:]);

def solution(info, query):
    answer = []
    infoDict = {}
    
    # 1. 'info'로 부터 나올 수 있는 모든 경우의 수
    # 를 조합(순열 X)하여 각각 맞는 조건에 점수를 추가한다.
    for i in info:
        i = i.split(' ')
        # print(i);
        value = int(i[-1]);
        for c in range(5):
            for case in combinations(i[:-1], c):
                key = ''.join(case);
                if key not in infoDict.keys():
                    infoDict[key] = [value];
                else: infoDict[key].append(value);
    # print(infoDict);
    
    # 2. 이진 탐색을 위한 모든 key에서의 값 정렬
    for k in infoDict.keys(): infoDict[k].sort();
    
    # 2. query에서 점수를 제외한 'key' 문자열을 찾음
    for q in query:
        q = q.replace(" and ", "").split(' ')
        key = q[0].replace('-','')
        standard = int(q[1])
        # print(key, standard);
        
        if key not in infoDict.keys():
            answer.append(0);
            continue;
        # values = sorted(infoDict[key]) (x)
        # print(values);
        answer.append(
            getCorrects(infoDict[key], standard));
    return answer
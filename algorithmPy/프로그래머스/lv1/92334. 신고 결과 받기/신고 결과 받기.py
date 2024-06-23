def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))];
    dictCounts = {userId : 0 for userId in id_list}
    dictReport = {}
    
    for r in report:
        r = r.split(' ');
        if (r[0] not in dictReport.keys()):
            dictReport[r[0]] = [r[1]];
            dictCounts[r[1]] += 1;
        else: 
            if (r[1] not in dictReport[r[0]]):
                dictReport[r[0]].append(r[1]);
                dictCounts[r[1]] += 1;
    # print(dictCounts);
    # print(dictReport);
    for user in id_list:
        for key in dictReport.keys():
            if (dictCounts[user] >= k
               and user in dictReport[key]):
                idx = id_list.index(key);
                answer[idx] += 1;
    return answer
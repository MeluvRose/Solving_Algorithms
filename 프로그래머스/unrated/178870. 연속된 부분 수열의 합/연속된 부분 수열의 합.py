def solution(sequence, k):
    answer = []
    idxs = [0 for i in range(2)]
    hap = sequence[0]
    lenSeq = len(sequence)
    
    # print(lenSeq);
    while(idxs[0] <= idxs[1] 
            and idxs[0] < lenSeq
            and idxs[1] < lenSeq):
        if hap > k:
            hap -= sequence[idxs[0]];
            idxs[0] += 1;
        else:
            if hap == k:
                answer.append(idxs[:]);
            if idxs[1] + 1 == lenSeq: break;
            hap += sequence[idxs[1] + 1];
            idxs[1] += 1;
    answer = sorted(answer, key = lambda x : x[1] - x[0])[0];
    return answer;
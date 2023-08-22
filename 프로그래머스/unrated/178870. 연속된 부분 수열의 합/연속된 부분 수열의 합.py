def solution(sequence, k):
    answer = []
    idxs = [0 for i in range(2)] # 'two pointers'
    hap = sequence[0] # 부분 수열의 누적합
    lenSeq = len(sequence)
    
    # sequence의 idxs[0]부터 idxs[1]까지의
    # 부분 수열을 범위를 바꿔가며 확인
    while(idxs[0] <= idxs[1] 
            and idxs[0] < lenSeq
            and idxs[1] < lenSeq):
        # 부분 수열의 누적 합이 클 때
        if hap > k:
            hap -= sequence[idxs[0]];
            idxs[0] += 1;
        else:
            # 부분 수열의 누적 합이 k와 같을 때
            if hap == k:
                answer.append(idxs[:]);
            # idxs[1]이 이미 sequence의 
            # last를 가리키고 있을 때
            if idxs[1] + 1 == lenSeq: break;
            hap += sequence[idxs[1] + 1];
            idxs[1] += 1;
    # 부분 수열들의 집합을 범위가 작은 순으로 정렬, 가장 작은 것을 선택
    answer = sorted(answer, key = lambda x : x[1] - x[0])[0];
    return answer;
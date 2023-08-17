def solution(progresses, speeds):
    answer = []
    features = progresses[:]
    
    while features:
        deploy = 0;
        for i in range(len(features)):
            features[i] += speeds[i];
        while features and features[0] >= 100:
            deploy += 1;
            features.pop(0);
            speeds.pop(0);
        if deploy > 0: answer.append(deploy);
    return answer

"""
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
"""
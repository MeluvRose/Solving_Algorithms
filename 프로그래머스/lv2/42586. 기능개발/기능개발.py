def solution(progresses, speeds):
    answer = []
    features = progresses[:]
    
    while features:
        deploy = 0;
        for i in range(len(features)):
            features[i] += speeds[i];
        # if features[0] >= 100:
        #     features.pop(0);
        #     speeds.pop(0);
        while features and features[0] >= 100:
            deploy += 1;
            features.pop(0);
            speeds.pop(0);
        if deploy > 0: answer.append(deploy);
    return answer
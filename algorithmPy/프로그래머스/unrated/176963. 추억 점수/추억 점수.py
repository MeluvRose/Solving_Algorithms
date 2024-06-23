def solution(name, yearning, photo):
    answer = []
    dictMissing = {n : yearning[idx] for idx, n in enumerate(name)}
    
    for p in photo:
        score = 0
        
        for n in p:
            if n in name: score += dictMissing[n];
        answer.append(score);
    return answer
def solution(participant, completion):
    # answer = ''
    participants = {p:0 for p in participant}
    
    for p in participant: participants[p] += 1;
    for c in completion: participants[c] -= 1;
    # print(participants);
    # print(participants.values());
    for p in participants:
        if (participants[p] != 0): return p; 
    # print(list(participants.values()));
    # answer = participant[idx];
    # return answer
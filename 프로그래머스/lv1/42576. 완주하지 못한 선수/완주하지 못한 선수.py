def solution(participant, completion):
    participants = {p:0 for p in participant}
    
    for p in participant: participants[p] += 1;
    for c in completion: participants[c] -= 1;
    for p in participants:
        if (participants[p] != 0): return p; 
    
"""
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""
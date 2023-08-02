def solution(players, callings):
    answer = []
    dictPlayers = {}
    dictRanks = {}
    
    for idx, player in enumerate(players):
        rank = idx + 1
        
        dictPlayers[player] = rank;
        dictRanks[rank] = player;
    for calling in callings:
        overtake = dictRanks[dictPlayers[calling] - 1]
        
        dictRanks[dictPlayers[calling]] = overtake;
        dictRanks[dictPlayers[overtake]] = calling;
        dictPlayers[calling] -= 1;
        dictPlayers[overtake] += 1;
    answer = list(dictRanks.values());
    return answer
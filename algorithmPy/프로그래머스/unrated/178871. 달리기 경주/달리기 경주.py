def solution(players, callings):
    player_ranks = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        current = player_ranks[call]
        
        player_ranks[call] -= 1;
        player_ranks[players[current - 1]] += 1;
        players[current - 1], players[current] = players[current], players[current - 1];
    return players;
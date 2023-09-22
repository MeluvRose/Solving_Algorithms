"""
트럭에 실을 수 있는 택배 상자의 최대 개수 : cap
배달할 집의 개수를 나타내는 정수 : n
각 집에 배달할 재활용 택배 상자의 개수를 담은 1차원 배열
=> deliveries
각 집에 수거할 빈 택배 상자의 개수를 담은 1차원 배열
=> pickups
"""

def solution(cap, n, deliveries, pickups):
    answer = 0
    visitedDeli = [False] * len(deliveries)
    visitedPick = [False] * len(pickups)
    stackDeli = deliveries[:]
    stackPick = pickups[:]
    
    # 실을 택배 상자가 없을 때,
    if (len(stackDeli) == stackDeli.count(0)
       and len(stackPick) == stackPick.count(0)):
        return answer;
    # 택배 상자가 존재하는 경우
    while stackDeli or stackPick:
        distance = (len(stackDeli) - 1
                   if len(stackDeli) > len(stackPick)
                   else len(stackPick) - 1) 
        boxDeli = 0
        boxPick = 0
        while (stackDeli 
               and cap >= boxDeli):
            if cap - boxDeli >= stackDeli[-1]:
                boxDeli += stackDeli.pop();
                continue;
            stackDeli[-1] -= (cap - boxDeli);
            boxDeli = cap;
            break;
        while (stackPick 
               and cap >= boxPick):
            if cap - boxPick >= stackPick[-1]:
                boxPick += stackPick.pop();
                continue;
            stackPick[-1] -= (cap - boxPick);
            boxPick = cap;
            break;
        answer += ((distance + 1) * 2);
    return answer;
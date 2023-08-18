from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = [0 for _ in range(bridge_length)]
    # onBridge = deque([0 for _ in range(bridge_length)]);
    
    sumBridge = 0 # 올라와 있는 트럭의 총 무게
    # truck_weights = deque(truck_weights);
    
    """
    1. 모든 트럭은 "bridge_length"만큼 이동해야 한다. 
    (초 당 1칸 이동)
    2. 트럭들은 다리의 지지 하중(weight)만큼 다리에 동시에
    오를 수 있다.
    (단, "bridge_length" 내에서 
    서로 다른 위치에 오르고 있다고 가정하려 한다.)
    """
    while (onBridge):
        # 대기하는 트럭이 존재하고, 다리에 오를 수 있는
        # 공간이 존재할 때,
        if (truck_weights
            and len(onBridge) < bridge_length):
            # 트럭의 무게 합이 weight 이하일 때,
            if sumBridge + truck_weights[0] <= weight:
                sumBridge += truck_weights[0];
                onBridge.append(truck_weights.pop(0));
            # weight 이상이라면, 빈 공간이 있을 거라고 표시
            else:
                onBridge.append(0);
        # 매 시간마다, 다리 위 트럭 무게 합과
        # 트럭 수의 현황을 연산
        sumBridge -= onBridge.pop(0);
        answer += 1;
    return answer
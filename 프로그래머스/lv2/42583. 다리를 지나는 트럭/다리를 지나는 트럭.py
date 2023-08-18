from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = [0 for _ in range(bridge_length)]
    # onBridge = deque([0 for _ in range(bridge_length)]);
    sumBridge = 0
    
    # truck_weights = deque(truck_weights);
    while (onBridge):
        if (truck_weights
            and len(onBridge) < bridge_length):
            if sumBridge + truck_weights[0] <= weight:
                sumBridge += truck_weights[0];
                onBridge.append(truck_weights.pop(0));
            else:
                onBridge.append(0);
        sumBridge -= onBridge.pop(0);
        answer += 1;
    return answer
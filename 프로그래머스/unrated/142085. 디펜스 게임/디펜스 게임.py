from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heappush(h, e)
        # print(e, n, h)
        
        # heap의 길이가 k보다 커질 때, 
        # pop을 실행 (가장 앞의 (작은) 값이 pop)
        # h(eap)에 남는 값은 enemy의 큰 값들이
        # 남아 있을 것(해당 경우에서 무적권을 쓴다고 생각)
        if len(h) > k:
            n -= heappop(h)
        # print(">>", n, h);
        
        # 더 이상 남는 병사가 없는 경우, 지금 순서(인덱스)
        # 에서 라운드가 종료된다고 답을 낼 수 있다.
        if n < 0:
            return i
    return len(enemy)
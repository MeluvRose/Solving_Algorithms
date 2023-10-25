def solution(routes):
    answer = 1
    endRoute = 30000 # 모든 차량이 갈 수 있는 제일 먼 지점
    
    # 가장 빨리 진입한 순으로 차량(경로) 정렬
    routes.sort(key=lambda x:x[0]);
    # print(routes);
    
    for s, e in routes:
        # 이전 경로 사이를 방문하지 않는 경우
        if s > endRoute:
            answer += 1;
            # 새로운 통과점을 탐색
            # (다음 차량(경로)부터 이전 경로를 지나치지 않기 때문)
            endRoute = e;
        
        # 이전 경로 사이를 방문하는 경우
        # 가장 빨리 진출하는 지점으로 변경
        endRoute = min(e, endRoute);
    return answer;
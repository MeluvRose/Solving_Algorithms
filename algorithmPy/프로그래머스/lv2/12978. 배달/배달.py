"""
N : 마을 개수 (1 <= N <= 50)
road : 도로정보(길이가 3인 배열)
    - 순서대로 (a, b, c)일 때, a,b는 도로가 연결하는
    두 마을의 번호, c는 도로를 지나는데 걸리는 시간
    (연결하는 도로가 여러 개 있을 수 있다. (최소를 찾으면?))
K : 음식 배달이 가능한 시간

(사용해야 하는 알고리즘)
https://chanhuiseok.github.io/posts/algo-50/
https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234424646&redirect=Dlog&widgetTypeCall=true&directAccess=false
"""
import heapq as hq

def solution(N, road, K):
    # 각 노드의 번호를 인덱스로 사용하기 위해 'N + 1'까지의 범위로
    # 최대 도착 가능 시간이 500,000이기 때문,
    graph = [[500001 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        graph[i][i] = 0
    
    # 'road'를 사용 최소 거리만 저장(중복이 있을 수 있기 때문)
    for a,b,k in road:
        graph[a][b] = min(graph[a][b],k)
        graph[b][a] = min(graph[b][a],k)
    
    # Floyd-Warshall
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
    
    answers = [x for x in graph[1] if x <= K]
    return len(answers)

"""
(BFS, 내가 했던 풀이)
from collections import deque

def solution(N, road, K):
    answer = 0
    dictRoad = {}
    
    def bfs(N, dictRoad, K):
        queue = deque()
        delivery = []
        visited = [False] * (N + 1)
    
        queue.append((1, 0));
        delivery.append(1);
        visited[1] = True;
        while queue:
            pre, t = queue.popleft();
            for i in range(1, N + 1):
                if (dictRoad[pre][i] > 0
                   and visited[i] == False
                   and t + dictRoad[pre][i] <= K):
                    queue.append((i, t + dictRoad[pre][i]));
                    delivery.append(i);
                    visited[i] = True;
        # print(delivery);
        return len(delivery);
                
    # 경로 설정
    for n in range(1, N + 1):
        dictRoad[n] = [0] * (N + 1)
    for a, b, c in road:
        if dictRoad[a][b] == 0:
            dictRoad[a][b] = c;
            dictRoad[b][a] = c;
            continue;
        dictRoad[a][b] = min(dictRoad[a][b], c);
        dictRoad[b][a] = min(dictRoad[b][a], c);
    # print(dictRoad);
    
    answer = bfs(N, dictRoad, K);
    return answer;
"""

"""
(Dijkstra)
import heapq

def dijkstra(dist,adj):
    # 출발노드를 기준으로 각 노드들의 최소비용 탐색
    heap = []
    heapq.heappush(heap, [0,1])  # 거리,노드
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in adj[node]:
            if cost+c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [cost+c,n])


def solution(N, road, K):
    dist = [float('inf')]*(N+1)  # dist 배열 만들고 최소거리 갱신할거임
    dist[1] = 0  # 1번은 자기자신이니까 거리 0
    adj = [[] for _ in range(N+1)]  # 인접노드&거리 기록할 배열
    for r in road:
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(dist,adj)
    return len([i for i in dist if i <=K])
"""
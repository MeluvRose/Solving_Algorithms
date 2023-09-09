from collections import deque

def solution(picks, minerals):
    answer = 0
    cntPicks = 0
    cntPicks = sum(picks)
    blocks = [[0, 0, 0] for x in range(10)]
    
    # 캘 수 있는 광물의 개수
    # for p in picks:
    #     cntPicks += p;
    # if len(minerals) > cntPicks * 5:
    #     minerals = minerals[:(cntPicks * 5)];
    minerals = minerals[:(cntPicks * 5)];
    
    # 광물 조사(분할)
    for idx in range(len(minerals)):
        if minerals[idx] == "diamond":
            blocks[idx // 5][0] += 1;
        elif minerals[idx] == "iron":
            blocks[idx // 5][1] += 1;
        else: blocks[idx // 5][2] += 1;
        
    # 피로도가 높은 조합 순으로(내림차순) 정렬
    blocks.sort(key=lambda x:(-x[0], -x[1], -x[2]));
    # print(blocks);
    
    # 피로도 계산
    for block in blocks:
        d, i, s = block
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0:
                picks[p] -= 1
                answer += (d + i + s)
                break;
            elif p == 1 and picks[p] > 0:
                picks[p] -= 1
                answer += ((5 * d) + i + s)
                break;
            elif p == 2 and picks[p] > 0:
                picks[p] -= 1
                answer += ((25 * d) + (5 * i) + s)
                break;
    return answer

"""

#     minerals = deque(minerals[:(5 * cntPicks)]);
#     for idx in range(len(picks)):
#         if picks[idx] > 0:
#             pick = pow(5, (2 - idx))
#             cnt = 0
#             while (cnt < 5 and len(minerals) > 0):
#                 cost = 0;
#                 m = minerals.popleft();

#                 # print(pick);
#                 if m == "diamond": cost = 25 // pick;
#                 elif m == "iron": cost = 5 // pick;
#                 # print(answer, cost);
#                 if cost <= 1: answer += 1;
#                 else: answer += cost;
#                 cnt += 1;
#             picks[idx] -= 1;
"""
def solution(picks, minerals):
    
    def dfs(picks, minerals, tired):
        nonlocal answer

        # print("before: ", picks);
        if sum(picks) == 0 or not minerals:
            answer = min(tired, answer)
            return

        for i in range(len(picks)):
            exp = 0
            if picks[i] >= 1:
                picks[i] -= 1
                mined = minerals[:5]
                if i == 0:
                    exp += len(mined)
                elif i == 1:
                    for mineral in mined:
                        if mineral == "diamond":
                            exp += 5
                        else:
                            exp += 1
                elif i == 2:
                    for mineral in mined:
                        if mineral == "diamond":
                            exp += 25
                        elif mineral == "iron":
                            exp += 5
                        else:
                            exp += 1
                dfs(picks, minerals[5:], tired + exp)
                picks[i] += 1
                # print("after: ", picks);
    answer = 25 * 55
    dfs(picks,minerals,0)
    return answer


"""
(구현)
def solution(picks, minerals):
    answer = 0
    cntPicks = sum(picks)
    blocks = [[0, 0, 0] for x in range(10)]
    
    # 캘 수 있는 광물의 개수
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
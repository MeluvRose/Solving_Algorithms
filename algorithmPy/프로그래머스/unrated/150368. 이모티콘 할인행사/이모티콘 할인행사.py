def combinationCase(prev):
    cases = []
    
    # print(prev);
    for li in prev:
        for n in [40, 30, 20, 10]:
            cases.append(li + [n]);
    return cases;

def solution(users, emoticons):
    answer = []
    cases = [[]]
    
    # 이모티콘 별 할인율 경우의 수 조합
    for _ in range(len(emoticons)):
        cases = combinationCase(cases);
    """
    percents = [10, 20, 30, 40]
    cases = product(percents, repeat=len(emoticons));
    """
    
    # 완전 탐색
    for case in cases:
        result = [0, 0]
        for percent, cost in users:
            price = 0
            for i in range(len(emoticons)):
                if case[i] >= percent:
                    price += (emoticons[i] // 100
                              * (100 - case[i]));
            if price >= cost: result[0] += 1;
            else: result[1] += price;
        answer.append(result);
    answer.sort(key=lambda x:(-x[0], -x[1]));
    return answer[0];

"""
(javaToPython)
lenUsers = None;
lenEmoticons = None;
discounts = [40, 30, 20, 10];
answer = []

def dfs(users, emoticons, arrDis, level):
    global lenUsers
    global lenEmoticons
    global discounts
    global answer
    
    # 현재 레벨(깊이)가 이모티콘의 총 개수와 같을 때,
    if level == len(emoticons):
        # print(arrDis);
        join = 0
        total = 0
        
        # 모든 할인율을 적용한 결과값 누적
        for i in range(lenUsers):
            cost = 0 # 유저 별 결제 예상 금액
            for j in range(lenEmoticons):
                if arrDis[j] >= users[i][0]:
                    cost += (emoticons[j] // 100 
                             * (100 - arrDis[j]));
            if cost >= users[i][1]: join += 1;
            else: total += cost; 
        answer.append([join, total]);
        return;
    # 이모티콘 별 할인율 적용 조합 계산
    for i in range(4):
        arrDis[level] = discounts[i];
        dfs(users, emoticons, arrDis, level + 1);
    return;
def solution(users, emoticons):
    global lenUsers 
    global lenEmoticons
    global answer
    lenUsers = len(users)
    lenEmoticons = len(emoticons)
    arrDis = [0] * lenEmoticons
    
    # for _ in range(lenEmoticons):
    #     answer.append([0] * 2);
    dfs(users, emoticons, arrDis, 0);
    # print(answer);
    answer.sort(key=lambda x:(-x[0],-x[1]));
    return answer[0];
"""
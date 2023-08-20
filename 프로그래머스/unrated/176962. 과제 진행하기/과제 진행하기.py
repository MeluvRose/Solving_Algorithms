def getTime(clock):
    HH, MM = map(int, clock.split(':'));
    
    return HH * 60 + MM;

def solution(plans):
    answer = []
    sections = [] # 분야(과제)
    remains = [] # 남은 시간
    clock = 0
    
    plans.sort(key=lambda x:x[1]);
    for p in plans:
        newClock = 0
        
        # 진행 중인 과제가 없을 경우,
        if not remains: clock = getTime(p[1]); 
        else:
            # 다음 과제가 시작하는 시간
            newClock = getTime(p[1]);
            while (remains and clock < newClock):
                # 남은 과제가 존재할 때, 가장 최근 과제부터
                # 새로운 과제가 시작하기 전에, 끝낼 수 있는 과제가
                # 있는지 체크
                if (newClock - clock >= remains[-1]):
                    clock += remains.pop();
                    answer.append(sections.pop());
                # 직전 과제가 끝나지 못할 경우, 남은 시간 재계산
                else: 
                    remains[-1] -= (newClock - clock);
                    break;
            clock = newClock;
        # 새로운 과제 및 진행 시간 추가
        sections.append(p[0]);
        remains.append(int(p[2]));
    # 모든 과제를 확인했을 때, 끝내지 못한 과제가 있다면,
    # 가장 최근에 중단했던 과제부터 끝내기 시작한다.
    while sections: answer.append(sections.pop());    
    return answer
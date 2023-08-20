def getTime(clock):
    HH, MM = map(int, clock.split(':'));
    
    return HH * 60 + MM;

def solution(plans):
    answer = []
    sections = []
    remains = []
    clock = 0
    
    plans.sort(key=lambda x:x[1]);
    for p in plans:
        newClock = 0
        
        if not remains: clock = getTime(p[1]); 
        else:
            # print(remains, p[1]);
            newClock = getTime(p[1]);
            # print(newClock - clock);
            while (remains and clock < newClock):
                # print(newClock, clock, remains[-1]);
                if (newClock - clock >= remains[-1]):
                    clock += remains.pop();
                    answer.append(sections.pop());
                else: 
                    remains[-1] -= (newClock - clock);
                    break;
            clock = newClock;
        sections.append(p[0]);
        remains.append(int(p[2]));
    # print(sections, remains);
    while sections: answer.append(sections.pop());    
    return answer
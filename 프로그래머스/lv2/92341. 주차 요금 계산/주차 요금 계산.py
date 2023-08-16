def getTime(pre, now = "23:59"):
    timeIn = pre.split(':')
    timeOut = now.split(':')
    hour = int(timeOut[0]) - int(timeIn[0])
    minute = int(timeOut[1]) - int(timeIn[1])
    
    return 60 * hour + minute;

def getFee(time, fees):
    extra = 0
    
    # 누적 주차 시간이 기본 시간 이하
    if time <= fees[0]: return fees[1];
    extra = ((time - fees[0]) / fees[2]);
    if extra % 1: extra = (extra // 1) + 1;
    return int(fees[1] + extra * fees[3]);

def solution(fees, records):
    answer = []
    times = {}
    cars = {}
    
    for r in records:
        record = r.split(' ');
        if record[2] == "IN":
            if (record[1] not in cars.keys()
                or cars[record[1]] == ''):
                cars[record[1]] = record[0]
                if record[1] not in times.keys():
                    times[record[1]] = 0;
                continue;
        else:
            times[record[1]] += getTime(cars[record[1]], record[0]);
            cars[record[1]] = '';
    for car in cars.keys():
        if cars[car] != '':
            times[car] += getTime(cars[car]);
    sortedKeys = sorted(times.keys())
    for key in sortedKeys:
        fee = getFee(times[key], fees);
        answer.append(fee);
    return answer
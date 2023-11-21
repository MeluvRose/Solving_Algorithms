# 기둥과 보는 길이가 1인 선분

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나 or 다른 기둥 위에 있어야 함
# 보는 한쪽 끝 부분이 기둥 위에 있거나 or 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함

def impossible(frame):
    for x, y, a in frame:
        # 기둥일 때,
        if a == 0:
            if (y != 0 
                and [x, y - 1, 0] not in frame
                and [x - 1, y, 1] not in frame
                and [x, y, 1] not in frame):
                return True;
            continue;
        if ([x, y - 1, 0] not in frame
           and [x + 1, y - 1, 0] not in frame
           and not (
                [x - 1, y, 1] in frame
                and [x + 1, y, 1] in frame
           )): return True;
    return False;

def demolition(frame, item):
    if item in frame:
        frame.remove(item);
        if impossible(frame):
            frame.append(item);
    return frame;

def building(frame, item):
    frame.append(item);
    if impossible(frame):
        frame.remove(item);
    return frame;

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        item = frame[:-1]
        # 건설일 때
        if frame[-1] == 1:
            answer = building(answer, item);
            continue;
        # 철거일 때
        answer = demolition(answer, item);
    return sorted(answer);
def solution(sizes):
    answer = 0
    tmp = []
    maxW = 0
    maxH = 0
    
    for size in sizes:
        if size[0] < size[1]: 
            tmp.append([size[1], size[0]])
            continue;
        tmp.append(size);
    for w, h in tmp:
        maxW = w if maxW < w else maxW;
        maxH = h if maxH < h else maxH;
    answer = maxW * maxH;
    return answer
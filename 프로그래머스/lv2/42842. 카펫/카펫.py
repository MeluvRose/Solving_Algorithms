def solution(brown, yellow):
    answer = []
    carpets = brown + yellow
    
    # 가장 바깥쪽의 카펫은 갈색으로 둘러싸여 있다.
    # 따라서, 노란색 격자가 중앙에 있기 위해선,
    # 가로의 격자가 3개 이상이어야 한다.
    for w in range(3, brown // 2):
        # 격자의 개수는 소수점이 될 수 없다
        if carpets % w > 0: continue;
        # print(w);
        h = carpets // w
        # print(w, h);
        if ((w - 2) * (h - 2) % yellow == 0
           and w >= h):
            answer = [w, h];
            break;
    return answer


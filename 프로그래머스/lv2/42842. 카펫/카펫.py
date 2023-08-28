def solution(brown, yellow):
    answer = []
    carpets = brown + yellow
    
    # 가장 바깥쪽의 카펫은 갈색으로 둘러싸여 있다.
    # 따라서, 노란색 격자가 중앙에 있기 위해선,
    # 가로의 격자가 3개 이상이어야 한다.
    for w in range(3, brown // 2):
        # 격자의 개수는 소수점이 될 수 없다
        if carpets % w > 0: continue;
        
        h = carpets // w
        if ((w - 2) * (h - 2) % yellow == 0
           and w >= h):
            answer = [w, h];
            break;
    return answer

"""
(수학)
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if red % i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]
                
(이분 탐색)
# x는 height, y는 width라고 하면,

# x * y = brown + yellow
# x + y = (brown + 4)//2

# x + y 에서 x, y를 정한다. 이때 x와 y의 차가 작을 수록 그 곱은 더 커진다.
# 이를 이용해서 이분 탐색으로 그 차의 크기를 조절해서 답을 구한다.

# x <= y 라고 하면, x는 1 ~ (x+y)//2 의 값을 가진다.
def solution(brown, yellow):
    m = brown + yellow
    s = (brown + 4) // 2

    # x가 가질 수 있는 최대값
    diff = (s // 2)

    # x가 가질 수 있는 최대값의 절반
    x = diff // 2
    y = s - x
    diff //= 2

    while x * y != m:
        if diff != 1:
            diff //= 2

        if x * y > m:
            x -= diff
            y += diff

        else:
            x += diff
            y -= diff

    return [y, x]
"""

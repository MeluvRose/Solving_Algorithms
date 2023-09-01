from collections import defaultdict

# 상한
def upperBound(weights, options):
    find = options[0]
    left = options[1]
    right = options[2]
    
    while (left < right):
        mid = (left + right) // 2;

        if (find < weights[mid]):
            right = mid;
        else: left = mid + 1;
    return left;

# 하한
def lowerBound(weights, options):
    find = options[0]
    left = options[1]
    right = options[2]
    
    while (left < right):
        mid = (left + right) // 2;

        if (find <= weights[mid]):
            right = mid;
        else: left = mid + 1;
    return left;

def solution(weights):
    answer = 0
    rates =[[1,1], [3,2], [4,2], [4,3]] 
    
    weights.sort();
    
    for rate in rates:
        for i in range(len(weights)):
            x = weights[i]
            
            # 가능한 비율로 y 값을 구함
            if x * rate[0] % rate[1] != 0:
                continue;
            y = x * rate[0] / rate[1]
            # y의 값이 i+1 부터 존재하는지 확인함
            upper = upperBound(weights, [y, i + 1, len(weights)])
            # 하한 탐색은 상한 탐색의 위치 이하이므로 탐색 마지막 위치를 upper 해도 됨
            lower = lowerBound(weights, [y, i + 1, upper])
            # 상한과 하한의 값을 빼서 중복된 값이 몇 개 인지 정답에 더함
            # 만약 y의 값이 범위 내에 존재하지 않으면,
            # 상한과 하한 둘 다 i+1의 위치를 반환하기 때문에 둘의 차이는 0이 될 것임
            answer += (upper - lower);
    return answer

"""
(memoization)

def solution(weights):
    answer = 0
    scales = defaultdict(int)
    
    weights.sort();
    for w in weights:
        answer += scales[w];
        answer += scales[w / 2];
        answer += scales[w * 2 / 3];
        answer += scales[w * 3 / 4];
        scales[w] += 1;
    return answer
"""
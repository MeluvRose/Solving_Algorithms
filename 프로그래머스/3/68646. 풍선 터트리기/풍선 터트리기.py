"""
n개의 풍선이 나열되어 있는 배열 a에서
풍선을 1개만 남길 수 있을 때까지 터뜨리고,
남겨질 수 있는 풍선은 몇 개인가?
- 임의의 인접한 풍선 2개 중 1개를 터트림
    - 2개 중 더 큰 숫자의 풍선을 터트려야 함.
    - 더 작은 풍선을 터트릴 수 있는 기회는 1번
- 터진 풍선의 공간은, 인접한 풍선으로 채운다.

* 인접한 풍선의 숫자가 모두 작으면 X
- 모든 원소 값을 기준으로 왼쪽, 오른쪽 풍선의 최솟값을 찾고,
해당 값들보다 기준 풍선의 숫자 값이 작지 않다면 마지막까지
남을 수 있다.
- 맨 왼쪽 or 오른쪽의 경우는 인접한 숫자가 더 작은 값일 경우가
최대 1개이다.
    - 인접한 숫자 중 최솟값을 만드는 것은 더 큰 숫자만을
    터뜨리면 남을 것이다.
    - 만약 인접한 최솟값이 기준 값보다 작을 경우, 숫자가 더 작은
    풍선은 1번 터뜨릴 수 있기 때문에, 기준 값보다 크던 작던
    상관이 X
    - 결론적으로, 풍선이 2개 이상 있다면, 최소 반환값은 2이다.

"""

def solution(a):
    answer = 0
    lenA = len(a)
    
    # 각 인덱스에서 왼쪽, 오른쪽의 최소값을 저장할 배열
    minLeft = [0 for _ in range(lenA)]
    minRight = [0 for _ in range(lenA)]
    
    # 왼쪽 or 오른쪽에서의 최소값
    l = a[0]
    r = a[lenA - 1]
    
    if lenA <= 2: return lenA;
    answer = 2;
    
    # 왼쪽의 최소값을 저장
    for i in range(1, lenA - 1):
        if (l > a[i]): l = a[i];
        minLeft[i] = l;
    
    # 오른쪽의 최소값을 저장
    for i in range(lenA - 2, 0, -1):
        if (r > a[i]): r = a[i];
        minRight[i] = r;
    # print(minLeft);
    # print(minRight);
    
    for i in range(1, lenA - 1):
        # 인접한 양 쪽의 숫자값이 모두 크면, 최후까지 남길 수 X
        if (a[i] > minLeft[i] and a[i] > minRight[i]):
            continue;
        answer += 1;
    return answer
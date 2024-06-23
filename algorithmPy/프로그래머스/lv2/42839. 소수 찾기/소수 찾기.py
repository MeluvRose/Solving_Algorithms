from itertools import permutations

global ok 
ok = list()

def is_prime_number(n):
    # tuple -> list -> str -> int
    nums = list(n)
    # string = ''.join(s for s in nums)
    string = ''.join(nums);
    num = int(string)
    # 소수 판별
    if num == 1 or num == 0 :
        return False
    for i in range(2,num):
        if (num % i == 0):
            return False
    ok.append(num)
    cnt = ok.count(num)
    print(ok, cnt);
    if (cnt >= 2):
        return False
    return True

def solution(numbers):
    ok = []
    answer = 0
    length = len(numbers)
    # 한 자리 수 부터, 전체 길이까지
    for i in range(1, length + 1):
        # permutations() : 전체 값에서 일정 길이의 
        # 부분 값 조합을 순차적으로 나열 (순열)
        for j in permutations(numbers,i):
            result = is_prime_number(j)
            if (result == True):
                answer += 1
    return answer
"""
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.
"""

limit = int(input())

if limit >= 0 and limit < 1001:
    i = 1
    hap = 0
    while hap < limit:
        hap += i
        i += 1
    print(i - 1)
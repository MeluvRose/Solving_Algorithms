"""
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
n번째 수를 출력하는 프로그램을 만들어보자.

#### 입력
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

#### 출력
n번째 수를 출력한다.
"""


val_input = list(map(int, input().split()))
nth = None

if len(val_input) == 4:
    a = val_input[0]
    m = val_input[1]
    d = val_input[2]
    n = val_input[3]

    for i in range(n):
        if not nth:
            nth = a
        else:
            nth = nth * m + d
    print(nth)
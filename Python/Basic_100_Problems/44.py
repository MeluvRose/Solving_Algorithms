"""
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.
"""

a, b = map(int, input().split())
print("%d\n%d\n%d\n%d\n%d\n%.2f" %(
    a+b, a-b, a*b, a//b, a%b, a/b))
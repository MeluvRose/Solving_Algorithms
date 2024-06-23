"""
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...
반복 실행구조를 사용해 보자.
"""

time = int(input())
while time > 0:
    print(time)
    time -= 1
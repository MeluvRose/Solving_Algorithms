"""
빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.  

#### 입력
빨녹파(r, g, b) 각 빛의 가짓수가 공백을 두고 입력된다.
예를 들어, 3 3 3 은 빨녹파 빛에 대해서 각각 0~2까지 3가지 색이 있음을 의미한다.
0 <= r,g,b <= 127

#### 출력
만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로
줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력한다.
"""

red, green, blue = map(int, input().split())
cnt_light = red * green * blue

for r in range(red):
    for g in range(green):
        for b in range (blue):
            print(r, g, b)
print(cnt_light)


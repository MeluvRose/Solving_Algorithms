"""
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
 3, 4, 5 : spring
 6, 7, 8 : summer
 9, 10, 11 : fall
"""
seasons = ["winter", "spring", "summer", "fall"]
month = int(input())

month_div_four = (month // 3 
    if (month // 3 > 0 and month // 3 < 4) 
    else 0)
print(seasons[month_div_four])

# def sumToN(n):
#     if n > 1:
#         return n + sumToN(n - 1);
#     return n;

def solution(n):
    answer = []
    # maxVal = sumToN(n)
    snail = [[0] * (i + 1) for i in range(n)]
    row, col = -1, 0
    val = 1
    # while val < (maxVal + 1):
    # for val in range(1, maxVal + 1):
    for i in range(n):
        """
        채우기 연산의 방향은 3가지 순서로 반복된다.
        1. 열(row) 이동: row++
        2. 행(col) 이동: col++
        3. 대각선 이동: row-- and col--
        그리고 횟수는 n, n-1, ..., 1만큼 이뤄진다.
        """
        move = n - i;
        for j in range(move):
            if i % 3 == 0: row += 1;
            elif i % 3 == 1: col += 1;
            else:
                row -= 1;
                col -= 1;
            # print(j, [row, col]);
            snail[row][col] = val;
            val += 1;
    # print(snail);
    for s in snail:
        answer.extend(s);
    return answer
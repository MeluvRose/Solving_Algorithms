def solution(wallpaper):
    answer = [];
    endX = 0;
    endY = 0;
    lenRows = len(wallpaper);
    lenCols = len(wallpaper[0])
    
    for r in range(lenRows):
        for c in range(lenCols):
            if wallpaper[r][c] == '#':
                print(r, c);
                if answer == []:
                    answer.append(r);
                    answer.append(c);
                    endX = r;
                    endY = c;
                    continue;
                if answer[0] > r: answer[0] = r;
                if answer[1] > c: answer[1] = c;
                if endX < r: endX = r;
                if endY < c: endY = c;
    answer.append(endX + 1);
    answer.append(endY + 1);
    return answer
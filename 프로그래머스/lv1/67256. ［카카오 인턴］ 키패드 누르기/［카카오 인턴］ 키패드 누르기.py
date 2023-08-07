def solution(numbers, hand):
    answer = ''
    keyPads = [['1', '2', '3']
               ,['4', '5', '6']
               ,['7', '8', '9']
               ,['*', '0', '#']]
    lHand = [3, 0];
    rHand = [3, 2];
    
    for num in numbers:
        target = chr(ord('0') + num)
        
        if (target == '1' or target == '4' 
            or target == '7'):
            lHand[1] = 0;
            answer += 'L';
            for row in range(len(keyPads)):
                if(target == keyPads[row][lHand[1]]):
                    lHand[0] = row;
                    break;
        elif (target == '3' or target == '6' 
            or target == '9'):
            rHand[1] = 2;
            answer += 'R';
            for row in range(len(keyPads)):
                if(target == keyPads[row][rHand[1]]):
                    rHand[0] = row;
                    break;
        else:
            point = []
            lLen = 0
            rLen = 0
            
            for row in range(len(keyPads)):
                for col in range(len(keyPads[0])):
                    if(target == keyPads[row][col]):
                        point = [row, col];
                        break;
            lLen = (abs(point[0] - lHand[0]) 
                    + abs(point[1] - lHand[1]));
            rLen = (abs(point[0] - rHand[0]) 
                    + abs(point[1] - rHand[1]));        
            if((lLen == rLen and hand == "right")
              or lLen > rLen): 
                rHand = point;
                answer += 'R';
            elif((lLen == rLen and hand == "left")
                or lLen < rLen): 
                lHand = point;
                answer += 'L';
    return answer
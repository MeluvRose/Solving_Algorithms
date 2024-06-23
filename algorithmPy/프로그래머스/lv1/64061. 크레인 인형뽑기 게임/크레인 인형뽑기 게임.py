def solution(board, moves):
    answer = 0
    bucket = [];
    
    for move in moves:
        item = 0;
        for i in range(len(board)):
            # 인형이 존재할 때만, 
            # 아래 연산들이 실행되어야 한다.
            if board[i][move - 1] != 0:
                item = board[i][move - 1];
                board[i][move - 1] = 0;
                bucket.append(item);
                break;
        if (len(bucket) > 1 
            and bucket[-2] == bucket[-1]):
            for i in range(2): bucket.pop();
            answer += 2;
    return answer
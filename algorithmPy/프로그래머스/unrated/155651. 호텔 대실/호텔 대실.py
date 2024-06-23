from heapq import heappop, heappush

def getTime(time):
    hour, minute = map(int, time.split(':'))
    
    return hour * 60 + minute;

def solution(book_time):
    answer = 0
    minutes = [0 for _ in range(60 * 24 + 10)]
    
    for book in book_time:
        start = getTime(book[0])
        end = getTime(book[1])
        minutes[start] += 1;
        minutes[end + 10] -= 1;
    num = 0
    for i in range(len(minutes)):
        num += minutes[i];
        minutes[i] = num;
    answer = max(minutes);
    return answer

"""
1. deque(queue)를 이용한 문제 접근(테케 O, 정답 X)
    bookQueue = deque()
    
    for start, end in book_time:
        item = []
        item.append(getTime(start));
        item.append(getTime(end));
        bookQueue.append(item);
    bookQueue = deque(
        sorted(bookQueue, key=lambda x:x[1]));
    while(answer < len(bookQueue)):
        if bookQueue[0][1] <= bookQueue[answer][0]:
            bookQueue.popleft();
            bookQueue = deque(
                sorted(bookQueue, key=lambda x:x[1]));
            continue;
        answer += 1;
        
2. 제출 코드 (heap)
    answer = 1
    bookTime = []
    
    # 문자형 -> 숫자형으로 변경
    for start, end in book_time:
        item = []
        item.append(getTime(start));
        item.append(getTime(end));
        bookTime.append(item);
    # 시작 시간 기준으로 정렬
    bookTime.sort();
    # bookTime.sort(key=lambda x:x[1]); (X)
    # print(bookTime);
    
    heap = []
    for s, e in bookTime:
        # print(heap, end = ' ');
        if not heap:
            heappush(heap,e + 10)
            # print(heap);
            continue
        # heap에 의해 heap[0]이 가장 빠른 종료 시각을 저장
        # heap[0] 보다 새로 입실할 시각이 같거나 느리다면
        # heap[0] 을 pop, 새로 할당할 공간 생성
        if heap[0] <= s:
            heappop(heap)
        # heap[0] 보다 새로 입실할 시각이 같거나 느리다면
        # heap에 할당할 원소의 예상 개수를 추가
        else:
            answer += 1
        # 새로 들어온 객실의 재입실 가능 시각을 추가 할당
        heappush(heap,e + 10)
        # print(heap);

2-1. list 활용
    bookTime = [[getTime(i[0]), getTime(i[1]) + 10] for i in book_time]
    rooms = []
    
    bookTime.sort();
    for book im bookTime:
        if not rooms:
            rooms.append(book)
            continue;
        for idx, room im enumerate(rooms):
            if book[0] >= room[1]:
                rooms[index] = room + book;
                break
        else: rooms.append(book);
    return len(rooms);
"""
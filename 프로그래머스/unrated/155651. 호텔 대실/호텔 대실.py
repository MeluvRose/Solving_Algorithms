from heapq import heappop, heappush

def getTime(time):
    hour, minute = map(int, time.split(':'))
    
    return hour * 60 + minute;

def solution(book_time):
    # answer = 0
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
"""
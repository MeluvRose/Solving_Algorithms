from heapq import heappop, heappush

def getTime(time):
    hour, minute = map(int, time.split(':'))
    
    return hour * 60 + minute;

def solution(book_time):
    # answer = 0
    answer = 1
    
    bookTime = []
    # bookQueue = deque()
    
    for start, end in book_time:
        item = []
        item.append(int(start[:2]) * 60 + int(start[3:]));
        item.append(int(end[:2]) * 60 + int(end[3:]));
        bookTime.append(item);
    bookTime.sort();
    # bookTime.sort(key=lambda x:x[1]);
    # bookQueue = deque(
    #     sorted(bookQueue, key=lambda x:x[1]));
    # while(answer < len(bookQueue)):
    #     if bookQueue[0][1] <= bookQueue[answer][0]:
    #         bookQueue.pop(0);
    #     answer += 1;
    # answer = len(bookQueue);
    
    
    heap = []
    for s, e in bookTime:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e + 10)
    return answer
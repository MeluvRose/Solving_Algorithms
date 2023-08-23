def solution(s):
    answer = []
    numbers = [0 for _ in range(100000)]
    number = ""
    for c in s:
        if (c >= '0' and c <= '9'):
            number += c;
            continue;
        if number != "":
            numbers[int(number) - 1] += 1;
            number = "";
    while (1):
        largest = max(numbers)
        idx = numbers.index(largest)
        if largest == 0: break;
        answer.append(idx + 1);
        numbers[idx] = 0;
    return answer
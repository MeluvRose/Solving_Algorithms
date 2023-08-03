def solution(n, lost, reserve):
    answer = 0
    students = [1 for i in range(n + 1)]
    idx = 0
    
    for l in lost: students[l] -= 1;
    for r in reserve: students[r] += 1;
    while (idx <= n):
        if (students[idx] == 0 
            and 2 in students):
            owner = 0;
            
            for i in range(idx - 1, n + 1):
                if (students[i] == 2): 
                    owner = i;
                    break;
            if (idx - 1 == owner
               or idx + 1 == owner):
                students[idx] += 1;
                students[owner] -= 1;
                present = owner + 1;
        idx += 1;
    print(students);
    for idx in range(1, n + 1):
        if (students[idx] != 0): answer += 1;
    return answer
def solution(n, lost, reserve):
    answer = 0
    students = [1 for i in range(n + 1)]
    idx = 0
    
    # 1. 도난 그리고 여유 현황 체크
    for l in lost: students[l] -= 1;
    for r in reserve: students[r] += 1;
    # 2. 탐색
    while (idx <= n):
        # 체육복이 없는 학생이 있을 때, 여유분이 있는지 체크
        if (students[idx] == 0 
            and 2 in students):
            owner = 0;
            
            # 여유분을 가지고 있는 학생의 번호를 체크
            # (단, 바로 직전 번호부터 확인한다.)
            for i in range(idx - 1, n + 1):
                if (students[i] == 2): 
                    owner = i;
                    break;
            # 체육복을 빌려줄 수 있는 경우, 연산 진행
            if (idx - 1 == owner
               or idx + 1 == owner):
                students[idx] += 1;
                students[owner] -= 1;
                present = owner + 1;
        idx += 1;
    # 체육 수업을 들을 수 있는 학생 수를 계산
    for idx in range(1, n + 1):
        if (students[idx] != 0): answer += 1;
    return answer

"""
💡 그리디 알고리즘 적용 (JAVA 예시)

1. 선택 절차 : 선택 과정에서 체육복을 읽어버린 학생과 여벌 체육복을 가져온 학생의 번호를 오름차순으로 정렬합니다.
2. 적절성 검사 : 체육복을 잃어버린 학생 중 여벌이 있는 학생에게 빌려줄 수 있는 학생 수를 계산하고, 그다음에는 체육복을 잃어버린 학생 중 여벌이 없는 학생에게 빌려줄 수 있는 학생 수를 계산합니다.
3. 해답 검사 : 체육복을 빌려 받은 학생 수를 계산하여 반환합니다.
/**
 * 그리디 알고리즘 : 체육복
 *
 * @return ResponseEntity<ApiResponse>
 * @link
 * @since 2023.06.24
 */
@GetMapping("/money")
public ResponseEntity<ApiResponse<Object>> changeMoney(int n, int[] lost, int[] reserve) {
    int answer = n - lost.length; // 체육복이 없는 학생 수

    // 1. 선택 절차
    // 학생 번호를 기준으로 정렬합니다.
    Arrays.sort(lost);
    Arrays.sort(reserve);

    // 2. 적절성 검사
    // 체육복을 잃어버린 학생 중 여벌이 있는 학생에게 빌려줄 수 있는 경우
    for (int i = 0; i < lost.length; i++) {
        for (int j = 0; j < reserve.length; j++) {
            if (lost[i] == reserve[j]) { // 여벌 체육복을 가진 학생이 체육복을 잃어버린 경우
                answer++; // 체육복을 빌려받은 학생 수 증가
                reserve[j] = -1; // 빌려준 학생은 더 이상 빌려줄 수 없도록 표시
                break;
            }
        }
    }
    // 3. 해답 검사
    // 체육복을 잃어버린 학생 중 여벌이 없는 학생에게 빌려줄 수 있는 경우
    for (int i = 0; i < lost.length; i++) {
        for (int j = 0; j < reserve.length; j++) {
            if (reserve[j] == lost[i] - 1 || reserve[j] == lost[i] + 1) {
                answer++;
                reserve[j] = -1;
                break;
            }
        }
    }

    ApiResponse<Object> ar = ApiResponse.builder()
            .result(answer)
            .resultCode(SUCCESS_CODE)
            .resultMsg(SUCCESS_MSG).build();
    return new ResponseEntity<>(ar, HttpStatus.OK);
}
"""
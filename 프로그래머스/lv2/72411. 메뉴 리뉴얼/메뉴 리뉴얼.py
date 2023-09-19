from itertools import combinations
from collections import Counter

"""
Counter 생성자는 여러 형태의 데이터를 인자로 받는데요. 먼저 
중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 
나오는지가 저장된 객체를 얻게 됩니다.
most_common()
"""

def solution(orders, course):
    answer = []
    menus = []
    
    # 개수 별 코스 메뉴 조합 구하기
    for c in course:
        temp = []
        
        for order in orders:
            # 주문이 항상 순서대로 배치되어 있지 X : 정렬 필요
            p = combinations(sorted(order), c)
            temp += list(p);
        # print(temp);
        counter = Counter(temp);
        
        # 코스의 메뉴 개수를 충족시키지 못하거나
        # 2명 이상의 손님으로부터 주문이 될 수 없는 경우
        if (len(counter) == 0 
            or max(counter.values()) < 2):
            continue;
        # print(counter);
        # 동일한 메뉴 개수라면, 더 많이 주문될 수 있는 것을 선택
        answer += [''.join(item) for item in counter 
                   if counter[item] == max(counter.values())]
    return sorted(answer);

"""
(DFS, C++)
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool cmp(pair<string, int> a, pair<string, int> b){
    return a.second > b.second;
}

void DFS(map<string, int>& dic, string& order, string comb, int index, int depth) {
    if (depth == comb.length()) {
        dic[comb]++;
        return;
    }

    for (int i = index; i < order.length(); i++) {
        comb[depth] = order[i];
        DFS(dic, order, comb, i + 1, depth + 1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    map<string, int> dic;

    for (int i = 0; i < orders.size(); i++) {
        sort(orders[i].begin(), orders[i].end());
        for (int j = 0; j < course.size(); j++) {
            string comb = "";
            comb.resize(course[j]);
            DFS(dic, orders[i], comb, 0, 0);
        }
    }
    
    vector<pair<string, int>> sorted;
    for (auto& order : dic) 
        if (order.second > 1)
            sorted.push_back(make_pair(order.first, order.second));
    sort(sorted.begin(), sorted.end(), cmp);
    
    for(int i = 0; i < course.size(); i++){
        int max = 0;
        for(int j = 0; j < sorted.size(); j++){
            if (sorted[j].first.length() != course[i]) 
                continue;
            else if (max == 0){
                answer.push_back(sorted[j].first);
                max = sorted[j].second;
            }
            else if (max == sorted[j].second)
                answer.push_back(sorted[j].first);
            else
                break;
        }
    }
    
    sort(answer.begin(), answer.end());
    return answer;
}
"""
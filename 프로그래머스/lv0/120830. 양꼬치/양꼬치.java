class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int sheep = 12000;
        int drink = 2000;
        
         k *= drink;
        
        for (int i = 1; i <= n; i++) {
            answer += 12000;
            if (i % 10 == 0) {
                k -= 2000;
            }
        }

        answer += k;
        
        return answer;
    }
}
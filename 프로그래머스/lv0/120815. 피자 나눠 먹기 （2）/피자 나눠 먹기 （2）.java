class Solution {
    public int solution(int n) {
        int answer = 1 + n / 6;
        
        if (n % 6 == 0) {
            answer--;
        }  
        
        return answer;
    }
}
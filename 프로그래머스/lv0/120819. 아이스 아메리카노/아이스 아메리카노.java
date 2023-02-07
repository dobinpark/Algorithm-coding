class Solution {
    public int[] solution(int money) {
        int[] answer = new int[2];
        int americano = 5500;                 // 아메리카노 가격
        int total = money / americano; // 최대 마실 수 있는 잔 수
        
        for (int i = 0; i < total; i++) {
            money -= americano;
        }
        
        answer[0] = total;
        answer[1] = money;
        
        return answer;
    }
}
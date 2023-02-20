class Solution {
    public int solution(int price) {
        int answer = 0;
       double  discount = 0;
        
        if (price >= 500000) {
            discount = Math.floor(price * 0.8);
            answer = (int)discount;
        } else if (price >= 300000 && price < 500000) {
            discount = Math.floor(price * 0.9);
            answer = (int)discount;
        } else if (price >= 100000 && price < 300000) {
            discount = Math.floor(price * 0.95);
            answer = (int)discount;
        } else {
            answer = price;
        }
        
        return answer;
    }
}
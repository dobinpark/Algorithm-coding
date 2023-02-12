class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = new int[num2 - num1 + 1];
        
       for (int i = num1, j = 0; i < num2 + 1; i++) {
            answer[j] = numbers[i];
           j++;
        }
        return answer;
    }
}
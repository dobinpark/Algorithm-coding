import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int pick = nums.length / 2;
        
        HashSet<Integer> hashSet = new HashSet<>();
        
        for(int n : nums)  {
	    	hashSet.add(n);
	    }
        
        if (hashSet.size() < pick) {
            answer = hashSet.size();
        } else {
            answer = pick;
        } 
        return answer;
    }
}
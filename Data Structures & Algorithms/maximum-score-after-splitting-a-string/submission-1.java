class Solution {
    public int maxScore(String s) {
        int zeros = 0;
        int ones = 0;
        int maxScore = 0;
        
        for (char c : s.toCharArray()){
            if (c == '1') ones++;
        }
        
        for (int i = 0; i < s.length()-1; i++){
            if (s.charAt(i) == '0') zeros++;
            if (s.charAt(i) == '1') ones--;
            int currentScore = zeros+ones;
            
            maxScore = Math.max(currentScore, maxScore);
        }

        return maxScore;
    }
}
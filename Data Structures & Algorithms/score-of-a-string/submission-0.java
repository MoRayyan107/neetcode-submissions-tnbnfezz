class Solution {
    public int scoreOfString(String s) {
        int score = 0;
        
        for ( int i = 1; i < s.length(); i++){
            int asciiA = (int)s.charAt(i-1);
            int asciiB = (int)s.charAt(i);
            
            score += Math.abs(asciiB-asciiA);
        }
                
        return score;
    }
}
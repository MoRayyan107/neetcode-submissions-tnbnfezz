class Solution {
    public boolean isSubsequence(String s, String t) {
        if (t.length() == 0){
            return false; 
        }

        if (s.length() == 0){
            return true;
        }

        int left = 0;
        int right = 0;

        while (left < s.length() && right < t.length()){

            // check if we found the chars matched if so increment the left 
            if (s.charAt(left) == t.charAt(right)){
                left++;
            }

            // alwas increment the right
            right++;
        }
        return left == s.length(); // if s is a subsequece of t the left value should be same as s.length
    }
}
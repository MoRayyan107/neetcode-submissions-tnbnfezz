class Solution {
    public int appendCharacters(String s, String t) {
        int left = 0;
        int right = 0;

        while(left<s.length() && right<t.length()){
            if (s.charAt(left) == t.charAt(right)){
                right++;  // move the t pointer if and only the char is found in s
            }

            left++;
        }

        int appendVals = t.length() - right;

        return appendVals;
    }
}
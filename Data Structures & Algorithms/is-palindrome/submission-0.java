class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        String replacedStr = s.replaceAll("[^a-z0-9]", "");

        int left = 0;
        int right = replacedStr.length()-1;

        while (left < right){
            if (replacedStr.charAt(left) != replacedStr.charAt(right))
                return false;

            left++;
            right--;
        }

        return true;
    }
}

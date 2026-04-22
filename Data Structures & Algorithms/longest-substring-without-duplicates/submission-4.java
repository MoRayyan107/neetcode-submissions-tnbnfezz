class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;

        if (s.length() == 0) return maxLen;

        int left = 0;
        int[] freq = new int[128];

        for (int right = 0; right < s.length(); right++){
            char ch = s.charAt(right);
            freq[ch]++;

            while (freq[ch]>1){
                char leftChar = s.charAt(left);
                freq[leftChar]--;
                left++;
            }

            maxLen = Math.max(right-left+1, maxLen);
        }

        return maxLen;
    }
}

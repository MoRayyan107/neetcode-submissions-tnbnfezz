class Solution {
    public int lengthOfLongestSubstring(String s) {

        if (s == null || s.length() == 0) return 0;
        
        int left = 0;
        int maxLen = 0;

        Map<Character, Integer> counts = new HashMap<>();

        for (int right = 0; right < s.length(); right++){
            char currentChar = s.charAt(right);
            counts.put(currentChar, counts.getOrDefault(currentChar, 0) + 1); // updating the curent value of the key

            while(counts.get(currentChar) > 1){
                char leftChar = s.charAt(left);
                counts.put(leftChar, counts.get(leftChar) - 1); // updating the curent value of the key
                left++;
            }

            maxLen = Math.max(maxLen, right-left+1);
        }

        return maxLen;
    }
}

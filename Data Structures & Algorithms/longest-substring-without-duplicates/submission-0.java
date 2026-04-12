class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLen = 0;

        Map<Character, Integer> lastSeenChars = new HashMap<>();

        for (int right = 0; right < s.length(); right++){
            char currentChar = s.charAt(right);

            if (lastSeenChars.containsKey(currentChar) && lastSeenChars.get(currentChar) >= left){
                left = lastSeenChars.get(currentChar) + 1; // shrinks the left window   
            }

            lastSeenChars.put(currentChar, right); // update the value
            maxLen = Math.max(maxLen, right-left+1);
        }

        return maxLen;
    }
}

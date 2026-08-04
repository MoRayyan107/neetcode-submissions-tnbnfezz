class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        maxWindow = 0
        mapMax = 0
        l = 0
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            mapMax = max(mapMax, freqMap[s[r]])

            if ( (r-l+1) - mapMax > k):
                freqMap[s[l]] -= 1
                l += 1
            
            mapMax = max(mapMax, freqMap[s[l]])
            maxWindow = max(maxWindow, r-l+1)
        
        return maxWindow
        
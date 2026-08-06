class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) == 0 or len(s) == 0 or len(t) > len(s):
            return ""

        tMap = {}
        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        distinctChars = len(tMap)
        
        print(f"tMap {tMap}, distinctChars: {distinctChars}")

        sMap = {}
        minLen = float('inf')
        bestIdx = [0,0]
        left = 0
        count = 0

        for right in range(len(s)):
            sMap[s[right]] = sMap.get(s[right], 0) + 1

            if s[right] in tMap and tMap[s[right]] == sMap[s[right]]:
                count += 1
            
            while left <= right and count == distinctChars:
                length = right-left+1
                if (length < minLen):
                    minLen = length
                    bestIdx[0], bestIdx[1] = left, right
                
                sMap[s[left]] -= 1
                if s[left] in tMap and sMap[s[left]] < tMap[s[left]]:
                    count -= 1
                left += 1

        return s[bestIdx[0]: bestIdx[1]+1] if minLen != float('inf') else ""
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) == 0 or len(s) == 0 or len(t) > len(s):
            return ""
        

        tMap = {}
        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        print("tMAP: ", tMap)

        sMap = {}
        matchCount = len(tMap)
        bestIndex = [0, 0]
        minLen = float("inf")
        count = 0

        print("Match to be done: ", matchCount)

        l = 0
        r = 0
        while r < len(s):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                count += 1

            print(sMap)
            print(count)

            while l <= r and count == matchCount:
                if ( r-l+1 < minLen):
                    minLen = r-l+1
                    bestIndex[0] = l
                    bestIndex[1] = r

                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    count -= 1

                l += 1 

            print("l:", l, " r:", r)

            r += 1

        if minLen == float('inf'):
            return ""
        else:
            return s[bestIndex[0]: bestIndex[1]+1]

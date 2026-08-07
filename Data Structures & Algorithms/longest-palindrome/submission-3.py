class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freqMap = {}
        leftOverChar = 0
        length = 0
        for i in range(len(s)):
            freqMap[s[i]] = freqMap.get(s[i], 0) + 1
        
        print(f"freqMap -> {freqMap}")

        for key, value in freqMap.items():
            print(f"Key -> {key}, Value -> {value}")
            pairs = value//2
            print(f"Key -> {key}, Pairs -> {pairs}")
            if pairs > 0:
                length += pairs*2
                print(f"length: {length}")
            if value % 2 > 0 or pairs == 0:
                leftOverChar += 1
                print(f"leftOverChar: {leftOverChar}")
        
        if leftOverChar >= 1:
            length += 1

        return length
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        res = ""

        maxLen = max(len(word1), len(word2))

        for i in range(maxLen):
            if left < len(word1):
                res += word1[left]
                left += 1
            if right < len(word2):
                res += word2[right]
                right += 1
        print(res)
        return res
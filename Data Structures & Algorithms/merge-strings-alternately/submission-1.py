class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # left = 0
        # right = 0
        # res = ""
        res = []

        maxLen = max(len(word1), len(word2))

        for i in range(maxLen):
            if i < len(word1):
                res.append(word1[i])
            #     left += 1
            if i < len(word2):
                res.append(word2[i])
            #     right += 1
        print(res)
        return "".join(res)
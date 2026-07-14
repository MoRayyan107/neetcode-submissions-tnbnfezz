class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set()
        maxCounter = 1
        for i in range(len(nums)):
            numSet.add(nums[i])

        for num in numSet:
            # print(num-1 not in numSet)
            if num-1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                maxCounter = max(maxCounter,length)
        # print(numSet)
        # print(counter, maxCounter)

        return maxCounter
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        print(nums)

        ## since im comparing 2 elements at same time there will be a by one of error 
        maxCount = 1
        count = 1
        for i in range(1, len(nums)):
            # print("count: ", count)
            # print(nums[i-1], nums[i])
            if nums[i] == nums[i-1]:
                # print("condition Duplicate")
                continue
            elif nums[i] == nums[i-1]+1:
                count += 1
            else:
                # print("Condition reset")
                maxCount = max(maxCount, count)
                count = 1

            maxCount = max(maxCount, count)
        return maxCount

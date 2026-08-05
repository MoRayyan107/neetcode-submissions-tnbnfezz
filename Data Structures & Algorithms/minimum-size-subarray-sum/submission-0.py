class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        minLen = float('inf')
        windowSum = 0

        for right in range(len(nums)):
            windowSum += nums[right]
            print(f"adding right {nums[right]} Sum -> {windowSum}")

            while windowSum >= target:
                minLen = min(minLen,right-left+1)
                # decrese till we actually find it 
                windowSum -= nums[left]
                left += 1

        if minLen == float('inf'):
            return 0
        else:
            return minLen
        
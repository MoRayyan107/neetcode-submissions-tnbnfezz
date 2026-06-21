class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            nums[i] = nums[i] ** 2
        
        left = 0
        right = n-1
        na = n-1

        newArray = [0] * n
        while left <= right:
            if nums[right] > nums[left]:
                newArray[na] = nums[right]
                right -= 1
            else:
                newArray[na] = nums[left]
                left += 1
            na -= 1

        return newArray
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)

        newArray = [0]*(length*2)

        for i in range(length):
            newArray[i] = nums[i]
            newArray[i+length] = nums[i]

        return newArray
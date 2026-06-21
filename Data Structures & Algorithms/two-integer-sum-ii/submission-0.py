class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        left = 0
        right = len(numbers) - 1

        while left < right:
            Sum = numbers[left] + numbers[right]
            if Sum == target:
                return [left+1,right+1] ## one indexed
            elif Sum > target:
                right -= 1
            else:
                left += 1
        return [] ## if not found
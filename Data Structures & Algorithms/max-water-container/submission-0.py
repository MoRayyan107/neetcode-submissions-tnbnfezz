class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        left = 0
        right = len(heights) - 1
        maxContainer = 0;

        while left < right:
            area = (right-left) * min(heights[left],heights[right])
            maxContainer = max(maxContainer, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxContainer                                                        
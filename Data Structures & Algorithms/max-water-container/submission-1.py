class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) -1
        maxArea = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            maxArea = max(maxArea, width*height)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else: # case when equal 
                right -= 1
        return maxArea
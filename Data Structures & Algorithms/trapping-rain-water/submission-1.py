class Solution:
    def trap(self, height: List[int]) -> int:
        length  = len(height)

        leftMax = [0] * length
        rightMax = [0] * length
        res = 0

        leftMax[0] = height[0]
        rightMax[length-1] = height[length-1]

        for i in range(1,length):
            leftMax[i] = max(leftMax[i-1], height[i])

        for i in range(length-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        for i in range(length):
            trap = min(leftMax[i], rightMax[i]) - height[i]

            if trap > 0:
                res+= trap

        # print(leftMax)
        # print(rightMax)
        # print(res)
        return res
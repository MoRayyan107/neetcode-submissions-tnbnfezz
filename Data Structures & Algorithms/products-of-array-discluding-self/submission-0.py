class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        # suppose nums => [1,2,3,4]
        # res = [0,0,0,0]
        prefix = 1
        postfix = 1

        # iter 0 => [1,0,0,0], prefix = 1
        # iter 1 => [1,1,0,0], prefix = 2
        # iter 2 => [1,1,2,0], prefix = 6
        # iter 3 => [1,1,2,6], prefix = 24 (we stop)
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # iter 0 => [1,1,2,6], postfix = 1
        # iter 1 => [1,1,8,6], postfix = 4
        # iter 2 => [1,12,8,6], postfix = 12
        # iter 3 => [24,12,8,6], postfix = 24 (we stop)
        for i in range(n-1, -1, -1):
            res[i] *= postfix # no need to override 
            postfix *= nums[i]
        
        return res
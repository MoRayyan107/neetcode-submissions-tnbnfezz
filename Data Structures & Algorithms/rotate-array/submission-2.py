class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## kinda made it optimised than brute forccing it 
        if k > 0:
            k = k % len(nums) # if k > len(nums) were technically gonna comebacck to original array 
            
            nums[:] = nums[-k:] + nums[:-k]
            #TC -> O(n) SCC-> O(n) (most probably)
 

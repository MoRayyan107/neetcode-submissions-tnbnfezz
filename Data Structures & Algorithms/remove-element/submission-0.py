class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # list[int] remove inplace
        # init the remove counter 
        counter = 0

        ## loop through the aray
        for i in range(len(nums)):

            ## if the value and the number are equal then increment the ccounter by 1
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
            
        # after the loop we just subtract the length by ccounter 
        return counter
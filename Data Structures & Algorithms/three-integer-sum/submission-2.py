class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the List
        # loop i from 0 to len-2
        # init 2 pointers
        nums.sort()
        res = []

        for i in range(len(nums)):

            # dup check if weve seen the same exxacct number before 
            if i>0 and nums[i-1] == nums[i]:
                continue #skip if equal

            left, right = i+1, len(nums)-1

            while left < right:
                tripletSum = nums[i]+nums[left]+nums[right]
                if tripletSum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                
                elif tripletSum > 0:
                    right -= 1
                elif tripletSum < 0:
                    left += 1

        
        return res
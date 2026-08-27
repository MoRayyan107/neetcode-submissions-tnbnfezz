class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sincce my last code was based on 2 Two pointers one outer and one inner
        ''' 
        that was a good shot but not worth it sincce itll miss many valid combinations since i was 
        forcing outer left and right to inccrement and decrement by 1 that broke the logic so
        Using a fixe value same in 3sum wher i was fixated to 0 and incremented once left < right 
        ''' 
        nums.sort()
        res = set()
        print(f"Sorted: {nums}")

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2): 
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1, len(nums)-1

                while left < right:
                    print(f"i: {i}, j: {j}, left {left}, right: {right}")
                    quadSum = nums[i]+nums[j]+nums[left]+nums[right]
                    print(quadSum)
                    
                    if quadSum == target:
                        print(f"Found it {[nums[i],nums[j],nums[left],nums[right]]}")
                        elems = tuple(sorted((nums[i],nums[j],nums[left],nums[right])))
                        res.add(elems)
                        left += 1
                        right -=1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left<right and nums[right] == nums[right+1]:
                            right -= 1
                    elif quadSum > target:
                        right -= 1
                    elif quadSum < target:
                        left += 1

        return list(res)
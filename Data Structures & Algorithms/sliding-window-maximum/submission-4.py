class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        left = 0

        for i in range(k):
            while len(dq) != 0 and nums[dq[-1]] < nums[i]:
                popedElem = dq.pop()
            dq.append(i)
        
        res.append(nums[dq[0]]) ## add the first element thats in deque 

        # now slide the window 
        for right in range(k, len(nums)):
            # print(f"right: {right}, left: {left}, len(dq): {len(dq)}, Current DQ: {dq}")
            # print(f"nums[dq[0]]: {nums[dq[0]]}, nums[dq[-1]]: {nums[dq[-1]]}")
            # print(f"nums[dq[-1]] < nums[right] {nums[dq[-1]] < nums[right]}")
            while len(dq) !=0 and nums[dq[-1]] < nums[right]:
                dq.pop()

            # if the idx is inside the dq remove it 
            if left in dq:
                dq.remove(left)
            left += 1

            # append the idx to dq
            dq.append(right)
            # append the value of idx into res
            res.append(nums[dq[0]])
            

        print(res)
        return res

        




class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()

        for i in range(k):
            while len(dq) != 0 and nums[dq[-1]] < nums[i]:
                popedElem = dq.pop()
            dq.append(i)
        
        res.append(nums[dq[0]]) ## add the first element thats in deque 

        # now slide the window 
        for right in range(k, len(nums)):
            # print(f"right: {right}, value: {nums[right]} len(dq): {len(dq)}, Current DQ: {dq}")
            # print(f"nums[dq[0]]: {nums[dq[0]]}, nums[dq[-1]]: {nums[dq[-1]]}")
            # print(f"nums[dq[-1]] < nums[right] {nums[dq[-1]] < nums[right]}")
            while len(dq) !=0 and nums[dq[-1]] < nums[right]:
                dq.pop()

            # if the idx is inside the dq remove it, from O(N) TO O(1)
            while dq and dq[0] < right - k + 1:
                dq.popleft()

            # append the idx to dq
            dq.append(right)
            # append the value of idx into res
            res.append(nums[dq[0]])
            

        print(res)
        return res

        




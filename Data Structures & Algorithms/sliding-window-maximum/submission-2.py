class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []

        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))

        res.append(-maxHeap[0][0])
        # print(maxHeap)

        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))

            # ccheckc for element who is outside the window
            # print(f"length -> {len(nums)}, i = {i}, k = {k}, i-k = {i-k}, is top maxxheap less-> {maxHeap[0][1] < i-k+1}")
            while maxHeap[0][1] < i-k+1:
                heapq.heappop(maxHeap)
            # print(maxHeap)
            
            res.append(-maxHeap[0][0])


        # print(res)
        return res

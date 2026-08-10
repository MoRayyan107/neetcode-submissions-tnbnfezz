import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        # print(heap)

        for i in range(k, len(nums)):
            # print(f"heap[0] = {heap[0]}")
            # print(f"nums[i] = {nums[i]}")
            # print(f"heap[0] < nums[i] => {heap[0] < nums[i]}") ## is nums[i] grater then pop and push

            if nums[i] < heap[0]:
                continue
            
            ## if its greater 
            heapq.heappushpop(heap, nums[i])
            # print(heap)

        return heap[0]

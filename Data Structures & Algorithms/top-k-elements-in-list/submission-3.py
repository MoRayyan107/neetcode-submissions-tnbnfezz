class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} 
        heap = []
        res = []

        for i in range(len(nums)):
            freqMap[nums[i]] = freqMap.get(nums[i], 0) + 1
        
        # print(f"freqMap => {freqMap}")

        for key, value in freqMap.items():
            heap.append((value, key))

        heapq.heapify(heap)
        # print(f"heap before popping {heap}")

        while len(heap) > k:
            heapq.heappop(heap)
        
        # print(f"heap => {heap}")

        while heap:
            value, key = heapq.heappop(heap)
            res.append(key)

        return res
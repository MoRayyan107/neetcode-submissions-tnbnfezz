class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} 
        heap = []
        res = []

        for i in range(len(nums)):
            freqMap[nums[i]] = freqMap.get(nums[i], 0) + 1
        
        # print(f"freqMap => {freqMap}")

        for key, value in freqMap.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))

            # if the heap lengt == k
            # check if the value (freq) are equal
            # if equal, check the key if thats the greatest, if yes pop and pus
            # if not, meaning value > the root, then pop and push
            elif len(heap) == k:
                if value == heap[0][0] and key > heap[0][1]:
                    heapq.heappushpop(heap, (value, key))
                elif value > heap[0][0]:
                    heapq.heappushpop(heap, (value, key))
                

        # for key, value in freqMap.items():
        #     heap.append((value, key))

        # heapq.heapify(heap)
        # # print(f"heap before popping {heap}")

        # while len(heap) > k:
        #     heapq.heappop(heap)
        
        # print(f"heap => {heap}")

        while heap:
            value, key = heapq.heappop(heap)
            res.append(key)

        return res
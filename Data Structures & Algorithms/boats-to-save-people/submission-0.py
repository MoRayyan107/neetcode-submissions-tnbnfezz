class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0
        
        countBoats = 0
        left = 0;
        right = len(people)-1
        people.sort()
        
        while (left < right):
            Sum = people[left] + people[right]
            if Sum <= limit:
                left += 1
                right -= 1
            else:   ## sum > limit
                right -= 1
            countBoats += 1
        
        if left == right:
            countBoats += 1
        
        print(countBoats)
        return countBoats
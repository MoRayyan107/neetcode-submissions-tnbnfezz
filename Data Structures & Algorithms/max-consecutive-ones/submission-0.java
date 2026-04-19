class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        int maxConsecutive = 0;
        int currentSequence = 0;

        for (int num : nums){
            if (num == 1) {
                currentSequence++;
            }

            if (num == 0){
                maxConsecutive = Math.max(maxConsecutive, currentSequence);
                currentSequence = 0;
            }
        }
        maxConsecutive = Math.max(maxConsecutive, currentSequence);
        
        return maxConsecutive;
    }
}
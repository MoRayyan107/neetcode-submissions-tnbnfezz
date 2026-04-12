class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> dupChecks = new HashMap<>();
        // {nums[i], num of appearences }

        for (int i = 0; i < nums.length; i++){
            if (dupChecks.containsKey(nums[i])){
                return true;           // if duplicate found
            }
            dupChecks.put(nums[i], 1);  // nums[i]. 1 -> nums[i] has appeared once 
        }

        return false; // if theres no duplicates
    }
}
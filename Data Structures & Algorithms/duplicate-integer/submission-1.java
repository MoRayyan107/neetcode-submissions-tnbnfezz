class Solution {
    public boolean hasDuplicate(int[] nums) {
        // New way using a hashSet
        Set<Integer> dupCheck = new HashSet<>();

        for (int i = 0; i < nums.length; i++){
            if (dupCheck.contains(nums[i])){
                return true;
            }

            dupCheck.add(nums[i]);
        }

        return false; // if no duplicates found
    }
}
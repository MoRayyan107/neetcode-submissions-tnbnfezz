class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1){
            return strs[0]; // empty if length off array is 1
        }

        String leader = strs[0]; // keep the leader on track 
        for (int i = 1; i < strs.length; i++){
            while (!strs[i].startsWith(leader)){
                leader = leader.substring(0, leader.length()-1);
            }

            if (leader.isEmpty())
                return "";
        }

        return leader;  
    }
}
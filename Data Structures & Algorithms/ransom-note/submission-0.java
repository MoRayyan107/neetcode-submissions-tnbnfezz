class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        int[] ransomFreq = new int[26];
        for (char c : magazine.toCharArray()){
            ransomFreq[c-'a']++;
        }

        for (char c : ransomNote.toCharArray()){
            if (--ransomFreq[c-'a'] < 0){
                return false;
            }
        }        

        return true;
    }
}
class Solution {
    public int lengthOfLastWord(String s) {
        if (s.length() == 1)
            return 1;

        String[] res = s.split(" ");
        int lastPos = res.length-1;

        return res[lastPos].length();
    }
}
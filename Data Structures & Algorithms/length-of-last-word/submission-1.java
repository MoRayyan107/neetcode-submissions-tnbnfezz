class Solution {
    public int lengthOfLastWord(String s) {
        if (s.length() == 1)
            return 1;

        // previous had a solutionn but hogs a lot of memory (but easier to read)

        int len = s.length() - 1;
        int count = 0;

        while( len >= 0 && s.charAt(len) == ' '){
            len--;
        }

        while( len >= 0 && s.charAt(len) != ' '){
            count++;
            len--;
        }

        return count;

    }
}
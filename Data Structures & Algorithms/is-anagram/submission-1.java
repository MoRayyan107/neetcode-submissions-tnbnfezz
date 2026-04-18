class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> anagramCount = new HashMap<>();

        for (char c : s.toCharArray()){
            anagramCount.put(c, anagramCount.getOrDefault(c,0) + 1);
        }

        for (char c : t.toCharArray()){
            anagramCount.put(c, anagramCount.getOrDefault(c,0) - 1);
            int countChar = anagramCount.get(c);

            if (countChar < 0){
                return false;
            }
        }

        return true;
    }
}

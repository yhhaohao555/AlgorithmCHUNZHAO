class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> dic = new HashMap<Character, Integer>();
        if (s.length() != t.length()) {
            return false;
        }
        for (char c: s.toCharArray()) {
            dic.put(c, dic.getOrDefault(c, 0) + 1);
        }
        for (char c: t.toCharArray()) {
            dic.put(c, dic.getOrDefault(c, 0) - 1);
            if (dic.get(c) < 0) {
                return false;
            }
        }
        return true;
    }
}
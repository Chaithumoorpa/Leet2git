class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = 0;
        int left = 0;

        Map<Character, Integer> window = new HashMap<>();

        for(int right=0; right<s.length(); right++){
            char ch = s.charAt(right);

            if(window.containsKey(ch)){
                left = Math.max(left, window.get(ch)+1);
            }
            window.put(ch,  right);

            len = Math.max(len, right-left+1);
        }

        return len;
    }
}
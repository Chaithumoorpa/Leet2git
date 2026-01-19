class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = dict()
        left =0 
        max_length = 0

        for right in range(len(s)):

            if s[right] in res  :
                left = max(left,res[s[right]]+1)
            
            res[s[right]] = right
            max_length = max(max_length, right - left +1)

        return max_length
        
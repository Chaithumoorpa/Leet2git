class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        for i in range(len(s)):
            # 1. Odd length palindromes (center is at 'i')
            count += self.expand(s, i, i)
            
            # 2. Even length palindromes (center is between 'i' and 'i+1')
            count += self.expand(s, i, i + 1)
            
        return count

    def expand(self, s, left, right):
        res = 0
        # Expand outward as long as the pointers are in bounds 
        # and the characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res
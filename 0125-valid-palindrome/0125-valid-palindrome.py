class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s= s.lower()
        l=[]
        for ch in s:
            if 'a' <= ch <= 'z' or  '0' <= ch <= '9':
                l.append(ch)
            
        s = "".join(l)
        

        left = 0
        right = len(s)-1
        while left < right:

            if s[left] != s[right]:
                return False
            
            left+=1
            right-=1
        
        return True
        
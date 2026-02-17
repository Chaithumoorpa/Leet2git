class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        index = 0
        n= len(s)
        while index < n // 2 :
            s[index], s[n-index-1] = s[n-index-1], s[index]
            index+=1
        return s
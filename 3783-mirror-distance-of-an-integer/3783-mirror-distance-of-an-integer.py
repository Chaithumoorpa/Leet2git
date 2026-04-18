class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Step 1: Reverse the digits
        # str(n)[::-1] reverses the string representation
        # int() converts it back, handling leading zeros automatically
        reversed_n = int(str(n)[::-1])
        
        # Step 2: Return the absolute difference
        return abs(n - reversed_n)
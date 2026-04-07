class Solution:
    def longestNiceSubstring(self, s):
        # Base case: A nice string must have at least a pair (length 2)
        if len(s) < 2:
            return ""
        
        # Convert to set for O(1) character lookups
        char_set = set(s)
        
        # Scan the string for any "illegal" characters
        for i, c in enumerate(s):
            # A character is illegal if its opposite case isn't in the set
            if c.swapcase() not in char_set:
                # Split the string at this character and solve for both sides
                sub1 = self.longestNiceSubstring(s[:i])
                sub2 = self.longestNiceSubstring(s[i+1:])
                
                # Return the longest one. 
                # If tied, sub1 is returned because it's the 'earliest' occurrence.
                return sub1 if len(sub1) >= len(sub2) else sub2
        
        # If the loop finishes, the entire current string is nice!
        return s
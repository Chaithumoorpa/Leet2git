class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = set(nums)
        
        # Duplicate = (Sum of nums) - (Sum of unique set)
        duplicate = sum(nums) - sum(s)
        
        # Missing = (Sum of 1...n) - (Sum of unique set)
        expected_sum = (n * (n + 1)) // 2
        missing = expected_sum - sum(s)
        
        return [duplicate, missing]
        
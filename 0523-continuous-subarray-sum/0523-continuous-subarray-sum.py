class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_map = {0: -1}
        
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            
            remainder = running_sum % k
            
            
            if remainder in remainder_map:
                
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                
                remainder_map[remainder] = i
                
        return False
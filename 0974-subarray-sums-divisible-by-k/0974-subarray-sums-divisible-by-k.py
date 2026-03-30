class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Map stores {remainder: frequency}
        remainder_map = {0: 1} # We've seen remainder 0 once (empty prefix)
        running_sum = 0
        total_count = 0
        
        for num in nums:
            running_sum += num
            remainder = running_sum % k
            
            # If this remainder was seen 3 times before, 
            # it forms 3 new valid subarrays ending here.
            if remainder in remainder_map:
                total_count += remainder_map[remainder]
                remainder_map[remainder] += 1
            else:
                remainder_map[remainder] = 1
                
        return total_count
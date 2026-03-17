class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        prod = 1
        left = 0
        count = 0
        for right in range(len(nums)):

            prod *= nums[right]

            while prod >= k and left <= right:

                prod //=nums[left]
                left+=1
            count += (right-left+1)

        return count


        
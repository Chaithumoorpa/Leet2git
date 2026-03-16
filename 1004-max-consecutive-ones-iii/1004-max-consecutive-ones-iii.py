class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        0 1 2 3 4 5 6 7 8 9 10
        l
        r
        1 1 1 0 0 0 1 1 1 1 0
        """

        left =0
        right =0
        max_ones = 0

        while right < len(nums):

            if nums[right] == 0:
                k-=1

            while k < 0:
                if nums[left] == 0:
                    k+=1
                left+=1
            
            max_ones = max(max_ones, right -left+1)
            right+=1
        return max_ones
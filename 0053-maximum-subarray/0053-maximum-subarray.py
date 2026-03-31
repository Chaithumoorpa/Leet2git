class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = nums[0]
        currSum =0

        for num in nums:

            currSum += num

            maxSum =  max(maxSum, currSum)

            if currSum < 0:
                currSum = 0
        

        return maxSum
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        current_sum = max_sum = sum(nums[:k])

        for i in range(len(nums)-k):

            current_sum += nums[i+k]-nums[i]
            max_sum = max(max_sum, current_sum)
        return float(max_sum)/k
        
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)

        smaller_count = {}

        for i, num in enumerate(sorted_nums):
            if num not in smaller_count:
                smaller_count[num] = i

        result = []

        for num in nums:
            result.append(smaller_count[num])

        return result
        
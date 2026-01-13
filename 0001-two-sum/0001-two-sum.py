class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()

        for i in range(len(nums)):

            if (target - nums[i]) not in res:
                res[nums[i]] = i
            else:
                return [res[target - nums[i]], i]
            

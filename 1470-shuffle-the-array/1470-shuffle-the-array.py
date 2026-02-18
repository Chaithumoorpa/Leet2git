class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        right = n
        res = list()
        for left in range(n):
            res.append(nums[left])
            res.append(nums[left+right])
        return res
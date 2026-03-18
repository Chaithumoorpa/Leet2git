class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 1:
            return nums
        
        res = []
        dq = deque()  # Stores indices
        
        for i in range(len(nums)):
            # 1. Remove indices of elements smaller than the current element
            # because they will never be the maximum in this or future windows
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # 2. Remove the front element if it's out of the window's range
            if dq[0] == i - k:
                dq.popleft()
            
            # 3. Once we've hit the window size k, start adding to results
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res
        
        """
        1 3 -1 -3 5 3 6 7

        0 1  2  3 4 5 6 7
                    k

        """

        
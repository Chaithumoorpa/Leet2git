class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findBound(isFirst):
            n = len(nums)
            low, high = 0, n - 1
            bound = -1
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        # Look left for a potential earlier start
                        high = mid - 1
                    else:
                        # Look right for a potential later end
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return bound

        return [findBound(True), findBound(False)]
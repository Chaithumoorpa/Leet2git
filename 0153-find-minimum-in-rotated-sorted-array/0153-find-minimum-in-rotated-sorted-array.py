class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        # If the array is not rotated at all
        if nums[left] <= nums[right]:
            return nums[left]
            
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the right element, 
            # the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than or equal to the right element, 
            # the minimum is in the left half (including mid)
            else:
                right = mid
                
        return nums[left]
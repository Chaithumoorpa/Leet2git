class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        ans = high
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Calculate total hours needed at speed 'mid'
            hours_needed = 0
            for pile in piles:
                # math.ceil(pile / mid) or (pile + mid - 1) // mid
                hours_needed += (pile + mid - 1) // mid
            
            if hours_needed <= h:
                # This speed works, try to find a smaller one
                ans = mid
                high = mid - 1
            else:
                # Too slow, must increase speed
                low = mid + 1
                
        return ans